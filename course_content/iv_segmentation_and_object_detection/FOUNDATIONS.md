# Foundations: segmentation and object detection for engineering measurement

This guide turns a computer-vision prediction into an engineering measurement. It complements—not replaces—the legacy U-Net and YOLO materials in the module README.

## 1. Start with the physical quantity

For a boiling image, a semantic-segmentation mask can estimate the projected vapor-area fraction in a stated region of interest (ROI):

$$
\phi_{\mathrm{vap}} =
\frac{A_{\mathrm{vap}}}{A_{\mathrm{ROI}}}
\approx
\frac{\sum_{i,j} m_{ij}}{N_{\mathrm{ROI}}},
$$

where $m_{ij}\in\{0,1\}$ is the vapor label for pixel $(i,j)$ and $N_{\mathrm{ROI}}$ is the number of pixels inside the ROI. The result is dimensionless. It is a projected image quantity, not automatically the three-dimensional void fraction. State the camera view, threshold/labeling rule, scale calibration, frame rate, and exclusions before comparing cases.

Object detection instead returns a set of boxes, commonly parameterized as $(x_c,y_c,w,h)$ in pixels plus a class score. A box can support a count or a location measurement; it does not provide the object boundary needed for projected area or shape.

## 2. What the network predicts

For binary segmentation, a model produces a probability $p_{ij}$ for every pixel. A threshold $\tau$ creates a mask:

$$
\hat m_{ij} =
\begin{cases}
1, & p_{ij}\geq \tau,\\
0, & p_{ij}<\tau .
\end{cases}
$$

The threshold is a measurement decision. Raising it may remove false vapor pixels but can also erase small bubbles. A common training loss is binary cross-entropy:

$$
\mathcal{L}_{\mathrm{BCE}} =
-\frac{1}{N}\sum_{i,j}
\left[m_{ij}\log(p_{ij})+
(1-m_{ij})\log(1-p_{ij})\right].
$$

Loss is optimized during training; it is not the physical measurement error. Compare predicted masks to held-out labels and inspect the resulting engineering quantity.

## 3. Evaluate spatial overlap

For predicted foreground pixels $P$ and reference foreground pixels $R$,

$$
\mathrm{IoU}=\frac{|P\cap R|}{|P\cup R|},
\qquad
\mathrm{Dice}=\frac{2|P\cap R|}{|P|+|R|}.
$$

Pixel accuracy can look high when most pixels are background. IoU and Dice expose whether the relatively small object of interest was actually recovered. For object detection, report a matching rule such as box IoU and then class precision/recall; do not treat an uncalibrated confidence score as a probability of physical correctness.

## 4. Worked representative case

Run the illustrative mask example:

<pre><code>python ../short_code_demos/segmentation.py</code></pre>

It returns $\mathrm{IoU}=2/3$ and $\mathrm{Dice}=0.8$. The predicted projected area is $2/9$ while the reference value is $3/9$: a one-pixel omission causes a one-third relative underestimation for this deliberately small object. In a real ROI, report both mask quality and the bias/error in $\phi_{\mathrm{vap}}$ over held-out frames or runs.

## 5. Minimal workflow

1. Define the measurement target, ROI, imaging geometry, and units.
2. Label a representative sample using a documented rule; preserve ambiguous-label decisions.
3. Split by run, specimen, operating condition, or acquisition session—not by nearly identical adjacent frames.
4. Train a baseline and inspect overlay images, false positives, and false negatives.
5. Convert held-out masks to the engineering quantity and compare with the reference calculation.
6. Evaluate a shifted condition: illumination, surface, heat flux, camera setting, material, or object size.

## Failure checks

- **Leakage:** Adjacent frames from one video appear in both training and testing.
- **Label ambiguity:** The model disagrees near an interface because annotators used inconsistent boundaries.
- **Class imbalance:** Background accuracy is high while small bubbles, cracks, or defects are missed.
- **Scale drift:** A changed magnification or ROI makes pixel area incomparable to the calibration case.
- **Domain shift:** Illumination, focus, specimen finish, or operating condition changes the image distribution.
- **Measurement overclaim:** A two-dimensional mask is reported as an unvalidated three-dimensional physical quantity.

## Transfer task

Replace the illustrative mask with a public-safe image problem from food inspection, additive manufacturing, robotics, or power-electronics inspection. Define the measured quantity first, then propose the label rule, split unit, overlap metric, and one condition that should remain completely held out.
