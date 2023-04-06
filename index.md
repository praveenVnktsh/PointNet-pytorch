## Assignment 5 

#### Praveen Venkatesh (pvenkat2)

Late Days: 
### Part 1

Accuracy of best model = 92.85%

<table>
<tr>
    <th>Correct Predictions</th>
    <td> <img src = "output/cls/gt_exp_0.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_700.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_900.gif" /> </td>
</tr>
<tr>
    <th>Incorrect Predictions</th>
   <td>  <img src = "output/cls/gt_exp_543.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_685.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_948.gif" /> </td>
</tr>

</table>

In the incorrect predictions, we can see that:
- Chair is predicted as a lamp
- Vase is predicted as a lamp
- Lamp is predicted as a vase



### Part 2

Accuracy of best model = 85.4%


<table>
<tr>
    <th>Predictions</th>
    <td> <img src = "output/seg/pred_exp_0.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_1.gif" /> </td>
  <td> <img src = "output/seg/pred_exp_2.gif" /> </td>
</tr>
<tr>
    <th>Accuracy</th>
    <td> 91.22</td>
    <td>95.43</td>
    <td>86.14</td>
</tr>
<tr>
    <th>Ground Truth</th>
    <td>  <img src = "output/seg/gt_exp_0.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_1.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_2.gif" /> </td>
</tr>
</table>

Poor Predictions:


<table>
<tr>
    <th>Predictions</th>
    <td> <img src = "output/seg/pred_exp_157.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_416.gif" /> </td>
  <td> <img src = "output/seg/pred_exp_595.gif" /> </td>
</tr>
<tr>
    <th>Accuracy</th>
    <td>36.98</td>
    <td>58.13</td>
    <td>49.34</td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_157.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_416.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_595.gif" /> </td>
</tr>
</table>

- We can see that the poor predictions are occuring where there is an intersection between different parts. This makes sense since the lines between different parts are not necessarily well defined (semantically) even though the dataset may be well defined. 
- In the case where there is a folding table on the chair, the model attempts to predicts two arms even though there is one!
- There are also subtle differences in predictions, especially in the first image where we can see that the dataset considers an extension of the leg into the sitting area as a part, whereas predictions cut off the legs of the chair only below the seating area. Both are equally valid interpretations from a semantic standpoint, as two different human annotators may label them in different ways.


### Part 3 Robustness analysis



##### Rotation Variation, Segmentation

I varied the rotation of the point clouds by 0, 5, 30 and 90 degrees. The accuracy of the model on the rotated point clouds is as follows:
<table>
<tr>
    <th>0 degree rotation</th>
    <td> <img src = "output/seg/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_100.gif" /> </td>
  <td> Accuracy = 86.4% </td>
</tr>
<tr>
    <th>5 degree rotation</th>
    <td> <img src = "output/seg_rotate_8/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_8/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_8/pred_exp_100.gif" /> </td>
  <td> Accuracy = 81.34% </td>
</tr>
<tr>
    <th>30 degree rotation</th>
    <td> <img src = "output/seg_rotate_52/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_52/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_52/pred_exp_100.gif" /> </td>
  <td> Accuracy = 64.94% </td>
</tr>
<tr>
    <th>90 degree rotation</th>
    <td> <img src = "output/seg_rotate_157/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_157/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_157/pred_exp_100.gif" /> </td>
  <td> Accuracy = 36.61% </td>
</tr>
</table>

Here, it is clear that the model is very sensitive to rotation, and cannot handle cases where the object is even slightly rotated without a big loss in accuracy. This is because our model does not encode any rotation invariant features.


##### Reduced Number of Points, Segmentation

<table>
<tr>
    <th>100 points</th>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_100.gif" /> </td>
  <td> Accuracy = 79.11% </td>
</tr>       
<tr>
    <th>500 points</th>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_100.gif" /> </td>
  <td> Accuracy = 85.21% </td>
</tr>
<tr>
    <th>1000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 87.03% </td>
</tr>
<tr>
    <th>5000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 86.75% </td>
</tr>

<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_500.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_600.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_100.gif" /> </td>
    <td> Accuracy = 86.4% </td>
</tr>
</table>

- We can see that the model is still able to predict classes with reasonable accuracy. This is likely because the datastet is such that all chairs have a canonical pose, and the model attempts to learn a general distribution of the classes over the space. This means that the model is evaluating the most likely class given a particular point, meaning that the model is able to predict the class correctly even if there are few points.



##### Rotation Variation, Classification

I varied the rotation of the point clouds by 0, 5, 30 and 90 degrees. Incorrect predictions are shown below:
<table>
<tr>
    <th>0 degree rotation</th>
    <td> <img src = "output/cls/gt_exp_499.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_600.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_100.gif" /> </td>
  <td> Accuracy = 92.85% </td>
</tr>
<tr>
    <th>5 degree rotation</th>
    <td> <img src = "output/cls8/pred_exp_721.gif" /> </td>
    <td> <img src = "output/cls8/pred_exp_619.gif" /> </td>
    <td> <img src = "output/cls8/pred_exp_646.gif" /> </td>
  <td> Accuracy = 86.53% </td>
</tr>
<tr>
    <th>30 degree rotation</th>
    <td> <img src = "output/cls52/pred_exp_721.gif" /> </td>
    <td> <img src = "output/cls52/pred_exp_646.gif" /> </td>
    <td> <img src = "output/cls52/pred_exp_619.gif" /> </td>
  <td> Accuracy = 62.22% </td>
</tr>
<tr>
    <th>90 degree rotation</th>
    <td> <img src = "output/cls157/pred_exp_157.gif" /> </td>
    <td> <img src = "output/cls157/pred_exp_168.gif" /> </td>
    <td> <img src = "output/cls157/pred_exp_216.gif" /> </td>
  <td> Accuracy = 28.41% </td>
</tr>
</table>

We can see once again that the model is highly sensitive to rotation as there is no rotation invariance baked into the architecture. Even slight changes in the pose of the object can lead to drastically different resutls.


##### Reduced Number of Points, Classification

<table>
<tr>
    <th>100 points</th>
    <td> <img src = "output/cls100/pred_exp_35.gif" /> </td>
    <td> <img src = "output/cls100/pred_exp_543.gif" /> </td>
    <td> <img src = "output/cls100/pred_exp_621.gif" /> </td>
  <td> Accuracy = 81.3% </td>
</tr>
<tr>
    <th>500 points</th>
    <td> <img src = "output/cls500/pred_exp_543.gif" /> </td>
    <td> <img src = "output/cls500/pred_exp_646.gif" /> </td>
    <td> <img src = "output/cls500/pred_exp_816.gif" /> </td>
  <td> Accuracy = 85.51% </td>
</tr>
<tr>
    <th>5000 points</th>
    <td> <img src = "output/cls500/gt_exp_500.gif" /> </td>
    <td> <img src = "output/cls500/gt_exp_600.gif" /> </td>
    <td> <img src = "output/cls500/pred_exp_670.gif" /> </td>
  <td> Accuracy = 92.93% </td>
</tr>
<tr>
    <th>10000 points</th>
   <td>  <img src = "output/cls/gt_exp_500.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_600.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_100.gif" /> </td>
    <td> Accuracy = 92.85% </td>
</tr>
</table>

We can see that the classification model is still able to perform reasonably well given low number of points. As the number of points increases, the model accuracy improves significantly. 



### Question 4 | Expressive Architectures

Here, I introduced some locality into the model by implementing KNN on each point and using it as a feature. Some specifics:
- Base PointNet model is used to generate global features.
- KNN on each input point is computed in the feature space. I have used 3 nearest neighbours. 
- The coordinates of points that are close together in the feature space is concatenated to the global feature vector and used to make predictions.


I trained it on the segmentation task. 

The model is able to achieve a test accuracy of 88.99%. 

We can see that the improvement is not very significant, this is likely because the number of added features after KNN aggregation is low. 
- The K parameter can be increased. This can potentially lead to improved performance.
- We can also note that the performance in early epochs is significantly better for the improved KNN model than the performance of the base pointnet model. We achieve around 78% accuracy within the first 5 epochs, whereas the pointnet model takes longer to achieve similar results.


Some image results:



<table>
<tr>
    <th>Predictions from Base Pointnet</th>
    <td> <img src = "output/seg/pred_exp_157.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_416.gif" /> </td>
  <td> <img src = "output/seg/pred_exp_595.gif" /> </td>
</tr>
<tr>
    <th>Predictions from PointNet with KNN</th>
    <td> <img src = "output/pointnetplus/pred_exp_157.gif" /> </td>
    <td> <img src = "output/pointnetplus/pred_exp_416.gif" /> </td>
  <td> <img src = "output/pointnetplus/pred_exp_595.gif" /> </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_157.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_416.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_595.gif" /> </td>
</tr>
</table>

We can see that the model with KNN features does a much better job with the more complex shapes that doesnt necessarily fit the general training distribution. The locality features added allows the model to use adjacent features to make better predictions and produce a more regularized result that matches the ground truth better. With more nearest neighbour features, it is likely that the model performs a better job!