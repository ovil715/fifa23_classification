## What this is about

Scraped www.fifaindex.com to get the in-game attributes for characters in FIFA 23.

Then, after some manipulation to simplify the number of positions (documented on line [22] of the jupyter notebook "Modeling.ipynb"),
we attempted to predict these positions using some machine learning models.

Models were initially selected on the basis of their theoretical 
suitability to the problem at hand (that is, a classification problem with multiple classes),
refined with Cross Validation
and subsequently evaluated according to the F1-score on the test set. 

The minimum baseline set was having an F1-score of 1 on the goalkeeper class (as in, no goalkeepers get confused by outfield players or the other way around).
Due to the difference of attributes between goalkeepers and outfield classes, we believe this to be a reasonable assumption for any model for this dataset.  SVM, Random Forest, KNN, and boosted trees, both ADA and XGB, passed this test.

From the confusion matrix displays, we can see there is a general difficulty to correctly classify some classes 
(in particular, central midfielders get confused with defensive midfielders, and strikers can be confused with attacking midfielders).
For the future, it could be interesting to check the performance on a simpler problem over the same dataset (as in classifying the line the player plays in: defender, midfield, forward).

The best performing model resulted to be an XGB classifier with learning rate of 0.05,
max tree depth of 7 and 180 estimators. It's weighted F1-score of 0.74 is substantially better
than the 0.49 of the Random Forest, and the 0.53 of ADABoost, while being marginally better than
the 0.66 of a linear SVC. Interestingly enough, a much more simpler model such as KNN
achieved a score of 0.69, which leaves open the debate about the tradeoff between performance and computational cost.