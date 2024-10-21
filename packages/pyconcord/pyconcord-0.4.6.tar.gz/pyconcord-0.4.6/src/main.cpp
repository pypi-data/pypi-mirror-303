#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/eigen/matrix.h>
#include <iostream>
using namespace std;

namespace py = pybind11;
using namespace Eigen;
using RowMatrixXd = Matrix<double, Dynamic, Dynamic, RowMajor>;
// Use RowMatrixXd instead of MatrixXd
// helper function to avoid making a copy when returning a py::array_t
// author: https://github.com/YannickJadoul
// source: https://github.com/pybind/pybind11/issues/1042#issuecomment-642215028
template <typename Sequence>
inline py::array_t<typename Sequence::value_type> as_pyarray(Sequence &&seq) {
  auto size = seq.size();
  auto data = seq.data();
  std::unique_ptr<Sequence> seq_ptr =
      std::make_unique<Sequence>(std::move(seq));
  auto capsule = py::capsule(seq_ptr.get(), [](void *p) {
    std::unique_ptr<Sequence>(reinterpret_cast<Sequence *>(p));
  });
  seq_ptr.release();
  return py::array(size, data, capsule);
}

double sgn(double val) {
  return (double(0) < val) - (val < double(0));
}

double sthresh(double x, double t ){
  return sgn(x) * max(abs(x)-t, 0.0);
}

void sthreshmat(MatrixXd & x,
    double tau,
    MatrixXd & t){
  
  MatrixXd tmp1(x.cols(), x.cols());
  MatrixXd tmp2(x.cols(), x.cols());
  
  tmp1 = x.array().unaryExpr(&sgn);
  tmp2 = (x.cwiseAbs() - tau*t).cwiseMax(0.0);

  x = tmp1.cwiseProduct(tmp2);

  return;
}

namespace _core {

typedef Triplet<double> T;

SparseMatrix<double, ColMajor> concord(const Ref<const RowMatrixXd> Y, //in: dense data
      optional<SparseMatrix<double, ColMajor>> x0,  
      // const Eigen::Ref<Eigen::VectorXi> I,                //in: sparse X
      // const Eigen::Ref<Eigen::VectorXi> J,                //in: sparse X
      // const Eigen::Ref<Eigen::VectorXd> V,                //in: sparse X
      double lambda1,                             //in: L1 penalty
      double lambda2,                             //in: L2 penalty
      double epstol = 1e-5,                      //in: convergence tolerance
      int    maxitr = 100,                       //in: maximum iterations allowed
      int    bb = 0)                             //in: use bb step (1:yes, 0:no)
{
  int n = Y.rows();
  int p = Y.cols();

  SparseMatrix<double, ColMajor> X(p, p);
  if (x0.has_value()) {
    X = x0.value();
  } else {
    vector<T> tripletList;
    tripletList.reserve(p);
    int index = 0;
    while (index < p) {
      tripletList.push_back(T(index, index, 1.));
      index++;
    }
    X.setFromTriplets(tripletList.begin(), tripletList.end());
  }
  DiagonalMatrix<double, Dynamic> XdiagM(p);
  SparseMatrix<double, ColMajor> Xn;
  SparseMatrix<double, ColMajor> Step;

  MatrixXd LambdaMat(p, p);
  LambdaMat.setConstant(lambda1);
  LambdaMat.diagonal().setZero().eval();

  MatrixXd S = (Y.transpose() * Y)/n;
  MatrixXd W = S * X;
  MatrixXd Wn(p, p);
  MatrixXd G(p, p);
  MatrixXd Gn(p, p);
  MatrixXd subg(p, p);
  MatrixXd tmp(p, p);
  
  double h = - X.diagonal().array().log().sum() + 0.5*(X.cwiseProduct(W).sum());
  if (lambda2 > 0) { h += (lambda2 * pow(X.norm(), 2)); } // elastic net

  double hn = 0; 
  double Qn = 0;
  // double f = 0;
  double subgnorm, Xnnorm, maxdiff;

  double tau;
  double taun = 1.0;
  double c = 0.5;
  int itr = 0;
  int loop = 1;
  int diagitr = 0;
  int backitr = 0;

  XdiagM.diagonal() = - X.diagonal();
  G = XdiagM.inverse();
  G += 0.5 * (W + W.transpose());
  if (lambda2 > 0) { G += lambda2 * 2.0 * X; } //elastic net
  
  while (loop != 0){
    
    tau = taun;
    
    diagitr = 0;
    backitr = 0;

    while ( 1 ) { // back-tracking line search

      if (diagitr != 0 || backitr != 0) { tau = tau * c; } // decrease tau only if needed

      tmp = MatrixXd(X) - tau*G;
      sthreshmat(tmp, tau, LambdaMat);
      Xn = tmp.sparseView();

      // make sure diagonal is positive
      if (Xn.diagonal().minCoeff() < 1e-8 && diagitr < 10) {
  diagitr += 1;
  continue;
      }

      Step = Xn - X;
      Wn = S * Xn;
      Qn = h + Step.cwiseProduct(G).sum() + (1/(2*tau))*pow(Step.norm(),2);
      hn = - Xn.diagonal().array().log().sum() + 0.5*(Xn.cwiseProduct(Wn).sum());
      if (lambda2 > 0) { hn += lambda2 * pow(Xn.norm(), 2); } //elastic net

      if (hn > Qn) { 
  backitr += 1;
      } else {
  break;
      }

    }

    XdiagM.diagonal() = - Xn.diagonal();
    Gn = XdiagM.inverse();
    Gn += 0.5 * (Wn + Wn.transpose()); //minus is in above line
    if (lambda2 > 0) { Gn += lambda2 * 2 * MatrixXd(Xn); }

    if ( bb == 0 ) {
      taun = 1;
    } else if ( bb == 1 ) {
      taun = ( Step * Step ).eval().diagonal().array().sum() / (Step.cwiseProduct( Gn - G ).sum());
    }

    tmp = MatrixXd(Xn).array().unaryExpr( &sgn);   // sign term
    tmp = Gn + tmp.cwiseProduct(LambdaMat);               // first term is in "tmp"
    subg = Gn;                                            // second term is in "subg"
    sthreshmat(subg, 1.0, LambdaMat);
    subg = (MatrixXd(Xn).array() != 0).select(tmp, subg); // select terms

    subgnorm = subg.norm();
    Xnnorm = Xn.norm();

    maxdiff = 0;
    for (int k=0; k<Step.outerSize(); ++k) {
      for (SparseMatrix<double>::InnerIterator it(Step,k); it; ++it) {
  maxdiff = max(abs(it.value()), maxdiff);
      }
    }

    X = Xn; 
    h = hn; 
    G = Gn;

    itr += 1;

    // loop = int((itr < maxitr) && (maxdiff > epstol) && (subgnorm/Xnnorm > epstol));
    // loop = int((itr < maxitr) && (maxdiff > epstol));
    loop = int((itr < maxitr) && (subgnorm/Xnnorm > epstol));

  }
  
  // int NNZ = X.nonZeros();
  // int i;

  // //memory allocation for sparse matrix output
  // VectorXi i_arr;
  // VectorXi j_arr;
  // VectorXd v_arr;

  // i = 0;
  // for (int k=0; k<X.outerSize(); ++k) {
  //   for (SparseMatrix<double,ColMajor>::InnerIterator it(X,k); it; ++it) {
  //     i_arr[i] = it.row();
  //     j_arr[i] = it.col();
  //     v_arr[i] = it.value();
  //     i++;
  //   }
  // }

 // end:
  return X;
}


PYBIND11_MODULE(_core, m) {
  m.doc() = "Python Bindings for _core";
  m.def("concord", &concord,
        "Covariance estimation using Concord "
        "",
        py::arg("Y"), 
        py::arg("x0") = py::none(), 
        py::arg("lambda1") = 0, py::arg("lambda2") = 0, py::arg("epstol") = 1e-5, py::arg("maxitr") = 100, py::arg("bb") = 0);
}

} // namespace _core


