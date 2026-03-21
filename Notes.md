

## 1. What it is

A parametric supervised learning algorithm used to model continuous target variables.  
Assumes that the dependent variable can be expressed as a linear combination of input features.  
“Linear” refers to linearity in parameters (weights), not necessarily in raw input space.

---

## 2. Model Representation

y = wᵀx + b

x ∈ ℝⁿ: feature vector  
w ∈ ℝⁿ: weight vector  
b: intercept term  

Prediction is a dot product plus offset.  

Equivalent matrix form:  
ŷ = Xw + b  

---

## 3. Objective

Minimize discrepancy between predicted values (ŷ) and actual values (y).  

Formally:  
min(w, b) L(w, b)

---

## 4. Loss Function (MSE)

L = (1/n) Σ (yᵢ − ŷᵢ)²  

Squares residuals ensure:  
Differentiability  
Strong penalty for large deviations  

Convex function → single global optimum  
Sensitive to outliers due to quadratic growth  

---

## 5. Optimization Methods

Normal Equation (Closed-form)  
Direct solution using linear algebra  
Expensive: O(n³) due to matrix inversion  
Not scalable for large feature sets  

Gradient Descent  
Iterative update:  
w := w − α ∇L  

Variants:  
Batch Gradient Descent  
Stochastic Gradient Descent  
Mini-batch Gradient Descent  

Requires learning rate tuning  

---

## 6. Assumptions (Statistical Validity)

Linearity: Expected value of y is linear in parameters  
Independence: Observations are not correlated  
Homoscedasticity: Constant variance of residuals  
No multicollinearity: Features not strongly correlated  
Normality of errors: Required for inference, not prediction  

Violation leads to unreliable coefficients or poor generalization  

---

## 7. Interpretation of Coefficients

wᵢ represents expected change in y per unit increase in xᵢ, holding others constant  

Magnitude indicates influence but depends on feature scale  
Standardization required for fair comparison  
Sign indicates direction of relationship  

---

## 8. Geometric View

Model fits a hyperplane in n-dimensional space  

Residual = vertical distance from actual point to predicted surface  

Optimization minimizes sum of squared vertical distances  
Not minimizing perpendicular distance  

---

## 9. Types

Simple Linear Regression  
One feature → straight line  

Multiple Linear Regression  
Multiple features → hyperplane  

Polynomial Regression  
Input features transformed (x², x³, etc.)  
Still linear in parameters  

---

## 10. Bias-Variance Tradeoff

High bias  
Model too simple → underfitting  

High variance  
Model too complex → overfitting  

Control mechanisms  
Reduce features → bias ↓, variance ↓  
Add features → bias ↓, variance ↑  
Regularization balances both  

---

## 11. Regularization

Adds penalty term to loss  

Ridge (L2)  
Shrinks weights smoothly  
Keeps all features  

Lasso (L1)  
Drives some weights to zero  
Performs feature selection  

Effect  
Reduces variance  
Slightly increases bias  
Improves generalization  

---

## 12. Sensitivity to Outliers

Squared error amplifies large residuals  

Outliers dominate optimization and skew results  

High-leverage points are especially dangerous  

Mitigation  
Remove or clip outliers  
Use robust regression methods  

---

## 13. Feature Scaling

Essential for gradient descent and regularization  

Without scaling  
Features with large magnitude dominate  
Slower convergence  

Methods  
Standardization (mean = 0, std = 1)  
Normalization (fixed range)  

---

## 14. Evaluation Metrics

MSE  
Optimization target, sensitive to outliers  

RMSE  
Same unit as target  

MAE  
Linear penalty, more robust  

R²  
Measures variance explained  
Range: (−∞, 1]  

---

## 15. When it works well

True relationship is approximately linear  
Noise is low and evenly distributed  
Features are meaningful and independent  
Interpretability is required  

---

## 16. When it fails

Strong non-linear patterns without transformation  
Multicollinearity leads to unstable coefficients  
Outliers distort fit  
High-dimensional data without regularization  

---

## 17. Residual Analysis

Residuals = y − ŷ  

Check for  
Patterns → non-linearity  
Funnel shape → heteroscedasticity  
Clusters → missing features  

Random scatter indicates good fit  

---

## 18. Core Intuition

Model finds parameters that minimize total squared error  

Equivalent to projecting data onto a linear subspace  

Tradeoff between fit accuracy and model simplicity  

---

## Summary

Linear regression is a linear parametric model optimized via MSE  

Strengths  
Interpretability  
Convex optimization  
Simplicity  

Limitations  
Rigid structure  
Sensitive to outliers  
Sensitive to feature correlation  
