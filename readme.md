# 3D-Printed Flexure Micro-Manipulator

This project contains an open source low-cost, easy-to-build **XYZ Micro-Manipulator** platform. 

It's designed for applications such as optical alignment, probing electronic components, and microscopy.
Thanks to its parallel kinematic structure and integrated flexures, it achieves good mechanical stiffness for a 3D-printed device, as well as micrometer precision.

<div style="display: flex;">
    <img src="images/CAD1.jpg" alt="Image 1" width="49%">
    <img src="images/Photo2.jpg" alt="Image 2" width="49%">
</div>

The design was partially inspired by another great open source flexure stage 'The OpenFlexure Block Stage - Sub-100 nm fibre alignment with a monolithic plastic flexure stage' 

### ✨ Examples

Below you find some examples of the translation stage in action. But there are many more possible use cases to be discovered...

<div style="display: flex;">
    <img src="images/Example_FiberCoupling.jpg" alt="Example 1" width="24%">
    <img src="images/Example_FiberAlignment.jpg" alt="Example 2" width="24%">
    <img src="images/Example_Microscopy.jpg" alt="Example 3" width="24%">
    <img src="images/Example_Drilling.jpg" alt="Example 3" width="24%">
</div>

<br><br>

### ⚙ CAD-Files

All CAD models are made in FreeCAD, to allow everyone to view and modify the design without subscribing or paying for a propriatary CAD solution.

<div style="display: flex;">
    <img src="images/FreeCAD_Model.jpg" alt="FreeCAD Model" width="50%">
</div>

<br>

The files for the metric version can be found here: [CAD Models Metric](construction_metric).
Please note that FreeCAD version **1.1.0dev** was used and the files might not work with older versions.

### ✅ 3D-Printing

Ready to print 3d-models are here: [Files for 3D-Printing](print_files/v2).

<div style="display: flex;">
    <img src="images/printed_parts.jpg" alt="Image 1" width="50%">
</div>

Parts are optimized for 0.4mm print nozzle and PLA. The parts 'WireMount' and 'FlexureStiffener' should be printed at slow speed (25mm/s) and with 0.1mm layerheight to ensure good quality prints.
All other parts can be printed with 0.2mm or 0.25mm layer height and regular speed. The endeffector requires a little bit of support, which is easy to peel of for this simple geometry.

### 📄Resources

Here are some great resources and similar projects from which inspiration for this project was drawn.

* [Open Flexure Microscope](https://openflexure.org/projects/microscope/)
* [The OpenFlexure Block Stage](https://arxiv.org/abs/1911.09986).

### 🚀 Contribute 

There are some open task for everyone wanting to contribute to this project:

* Create CAD model for imperial units.
* Improve O-Ring Flexure preload mechanism.
* Find an easy way to mount the crank wheels true and without 'wobble' to M3 bolts.
* Create useful endeffector attachments and grippers.

