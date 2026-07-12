#SHAP (SHapley Additive exPlanations)
#it edxplain the why the model give this result
# it is done after the mode is trained

#After training a tree-based model (such as Random Forest or XGBoost),
#  you can use SHAP like this:
import shap

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

#for visualization 
shap.summary_plot(shap_values, X_test)
