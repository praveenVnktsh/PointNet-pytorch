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



### Part 2

Accuracy of best model = 89.4%


<table>
<tr>
    <th>Predictions</th>
    <td> <img src = "output/seg/pred_exp_0.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_0.gif" /> </td>
  <td> <img src = "output/seg/pred_exp_0.gif" /> </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_0.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_0.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_0.gif" /> </td>
</tr>
</table>

Poor Predictions:


<table>
<tr>
    <th>Predictions</th>
    <td> <img src = "output/seg/pred_exp_573.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_484.gif" /> </td>
  <td> <img src = "output/seg/pred_exp_229.gif" /> </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_573.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_484.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_229.gif" /> </td>
</tr>
</table>


### Part 3 Robustness analysis



##### Rotation Variation, Segmentation

I varied the rotation of the point clouds by 0, 5, 30 and 90 degrees. The accuracy of the model on the rotated point clouds is as follows:
<table>
<tr>
    <th>0 degree rotation</th>
    <td> <img src = "output/seg/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>5 degree rotation</th>
    <td> <img src = "output/seg_rotate_8/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_8/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_8/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>30 degree rotation</th>
    <td> <img src = "output/seg_rotate_52/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_52/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_52/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>90 degree rotation</th>
    <td> <img src = "output/seg_rotate_157/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_rotate_157/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_rotate_157/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_500.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_600.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_100.gif" /> </td>
    <td> Accuracy = 89.4% </td>
</tr>
</table>

We can see that the model is able to perform segmentation even when the number of points is low. 


##### Reduced Number of Points, Segmentation

<table>
<tr>
    <th>100 points</th>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>       
<tr>
    <th>500 points</th>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>1000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>5000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>

<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_500.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_600.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_100.gif" /> </td>
    <td> Accuracy = 89.4% </td>
</tr>
</table>


##### Rotation Variation, Classification

I varied the rotation of the point clouds by 0, 5, 30 and 90 degrees. Incorrect predictions are shown below:
<table>
<tr>
    <th>0 degree rotation</th>
    <td> <img src = "output/cls/gt_exp_499.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_600.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>5 degree rotation</th>
    <td> <img src = "output/cls8/pred_exp_721.gif" /> </td>
    <td> <img src = "output/cls8/pred_exp_619.gif" /> </td>
    <td> <img src = "output/cls8/pred_exp_646.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>30 degree rotation</th>
    <td> <img src = "output/cls52/pred_exp_721.gif" /> </td>
    <td> <img src = "output/cls52/pred_exp_646.gif" /> </td>
    <td> <img src = "output/cls52/pred_exp_619.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>90 degree rotation</th>
    <td> <img src = "output/cls157/pred_exp_157.gif" /> </td>
    <td> <img src = "output/cls157/pred_exp_168.gif" /> </td>
    <td> <img src = "output/cls157/pred_exp_216.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/cls/gt_exp_500.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_600.gif" /> </td>
    <td> <img src = "output/cls/gt_exp_100.gif" /> </td>
    <td> Accuracy = 89.4% </td>
</tr>
</table>


##### Reduced Number of Points, Segmentation

<table>
<tr>
    <th>100 points</th>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_100/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>500 points</th>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_500/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>1000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>5000 points</th>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_500.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_600.gif" /> </td>
    <td> <img src = "output/seg_lowpoints_1000/pred_exp_100.gif" /> </td>
  <td> Accuracy = 89.4% </td>
</tr>
<tr>
    <th>Ground Truth</th>
   <td>  <img src = "output/seg/gt_exp_500.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_600.gif" /> </td>
    <td> <img src = "output/seg/gt_exp_100.gif" /> </td>
    <td> Accuracy = 89.4% </td>
</tr>
</table>

