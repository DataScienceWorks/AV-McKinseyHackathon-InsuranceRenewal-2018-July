# Solutioning

### FAQs

* What is the relevance of p_benchmark in this problem?

  > p_benchmark is decided by the company. You can consider it as the best solution for the problem. More accurate your model, closer you are to the p_benchmark.

* Is the incentive is decided to make maximum policies to be renewed as well as optimising the total profit?

  > The incentive plan is for agents, to maximize the revenue. The incentive will be given to the agents to collect the renewals. Using incentives provided, efforts (in hours) can be calculated. 
  >
  > In other words, if you give an agent 'x' incentive, he will put in 'y hours' of effort. Now you have to decide how much incentive should be given for each person (or how many hours of effort is required) to increase the chance of renewal.

* When we say perc premium paid by cash or CC, what are the two ends of the scale? What does 0 and 1 mean?

  > Of the total premium, what percentage was paid in cash or credit card, can be determined by the values in this column.  These are percentage values, and hence the range is between 0 and 1.
  >
  > The client considers payment by cash/credit  or payment by other methods (emi, online payment) as an important feature in deciding the chances of renewals.
  >
  > Most likely, the other method is automatic checks. Pretty common for insurance, and renewal is usually automatic with this method as well. Probably has an effect on renewal rates.

* 



### ML Topics

#### ROC Curve

An **ROC curve** (**receiver operating characteristic curve**) is a graph showing the performance of a classification model at all classification thresholds. This curve plots two parameters:

- True Positive Rate
- False Positive Rate

To compute the points in an ROC curve, we could evaluate a logistic regression model many times with different classification thresholds, but this would be inefficient. Fortunately, there's an efficient, sorting-based algorithm that can provide this information for us, called AUC. 



#### AUC : Area under Curve (the ROC Curve)

**AUC** stands for "Area under the ROC Curve." That is, AUC measures the entire two-dimensional area underneath the entire ROC curve (think integral calculus) from (0,0) to (1,1). 

