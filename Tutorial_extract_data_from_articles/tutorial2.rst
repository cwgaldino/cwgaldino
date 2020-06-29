#########################################
Extract data from figures using Inkscape
#########################################

.. sidebar:: title

    .. container:: cc

        .. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
            :target: http://creativecommons.org/licenses/by/4.0/
            :width: 80px

        This work is licensed under a `Creative Commons Attribution 4.0 International License`_.

.. _`Creative Commons Attribution 4.0 International License`: http://creativecommons.org/licenses/by/4.0/

**Carlos Galdino**

Last updated: |date|

.. |date| date::


In this tutorial, we are going to extract data from figures in pdf’s using a vector graphics editor (`Inkscape`_), a text editor (`Atom`_), and a spreadsheet software (`LibreOffice Calc`_). Note that, this method is not bound by this choice of applications and you may use your preferred ones.

As an example, I have created this `dummy pdf article`_ which we will use trough out this tutorial. The example article has figures with graphs using either solid curves or scattered points. Also, half of the figures are in a `vector`_ format and the other half are in a `raster`_ format. Roughly speaking, the main difference between them is that raster graphics (.png, .jpg, ...) are made of pixels, while vector graphics (.svg, .eps, ...) are made of vector Cartesian points. In the figure below we can clearly see the difference between them. Note that, no matter how much you zoom in on the figure below, there is no blur in the vector part. This is what makes vector format perfect for high-quality publication figures or presentation on big screens. Raster images should be preferred mostly when the image is a photograph (sometimes heatmaps are also better presented using raster format).

.. _Inkscape: https://inkscape.org/
.. _Atom: https://atom.io/
.. _LibreOffice Calc: https://www.libreoffice.org/discover/calc/
.. _dummy pdf article: tutorial/article_example.pdf
.. _vector: https://en.wikipedia.org/wiki/Vector_graphics
.. _raster: https://en.wikipedia.org/wiki/Raster_graphics


.. image:: raster_vector.svg
    :target: raster_vector.svg
    :width: 600px

The figure above is a montage of figures 1 and 3 in the example pdf. Be aware that, we can only extract data from vector images, so there is this other tutorial that will show you `how to convert raster images (graphs) to a vector format`_. Also, we need the figure to be formed by solid lines. If the curves are represented by scattered points, as in figures 2 and 4 in the example article, we have to transform them into solid lines in a vector format.

.. _how to convert raster images (graphs) to a vector format: ../Tutorial_raster2vector/test.html

Step-by-step instructions
=======================================

1. Download, install and open Inkscape.

2. Click and drag the pdf file into Inkscape.

tutorial_html_4228efbc467b1e45.gif

3. Zoom in on figure 1, click over it couple of times until the figure is selected. Then, drag it elsewhere so you can select and delete the everything else.

tutorial_html_316260eee02f956c.gif

4. Check if the figure is a “clone”. You may check at the status bar down below
after selecting the image. If the image is a clone, with the image selected, go to <span style="font-variant: normal"><span style="font-style: normal">Edit
</span></span><span style="font-variant: normal"><font face="cmmi10"><span style="font-style: normal">&gt; </span></font></span><span style="font-variant: normal"><span style="font-style: normal">Clone </span></span><span style="font-variant: normal"><font face="cmmi10"><span style="font-style: normal">&gt; </span></font></span><span style="font-variant: normal"><span style="font-style: normal">Unlink Clones recursively.

tutorial_html_ff8d7aeb626347b5.gif

.. Note::

    Sometimes, when importing figures from pdf’s, new objects may disappear outside of the “figure area”. I think that is a bug in which the “layers” of the svg file are not formatted properly. If this bothers you, a possible fix is to just add a new layer and ungroup the objects.

5. Use the nodes tool to select all nodes in the curve. Then, with all nodes selected, click in the button add nodes. This will add one extra node between two existing nodes. You may click the add nodes button more than once to increase the number of nodes (in this case twice is enough). Finally, transform all nodes to segment lines by clicking the button “Make selected segments lines”. Sometimes, I notice that to click this button only once do not work (maybe this is something of early versions of Inkscape,), so I like to make segments lines, then make selected nodes symmetric, then making them segments lines again.

tutorial_html_e6c318f98cafc72e.gif

6. Check the name of the objected of interest. In this case, the red curve. Click on the curve (you may need to click more then once to select the curve,
because there is a high change the different objects are grouped), then open the Objects dialog in Objects<span style="font-variant: normal"> </span><span style="font-variant: normal"><font face="cmmi10"><span style="font-style: normal">&gt; </span></font></span>Objects. In this case, the name of the red curve is “path16271”.

tutorial_html_26ca99603157a73a.gif

. Save the file. I saved as drawing.svg.

8. Download, Install, and open Atom. Or you may use any other text editor as long as it has the ability to find and replace text.

9. Open Drawing.svg in Atom. We may do that by clicking and draging the .svg file to Atom.

tutorial_html_e601c82b1336913.gif

10. Find “path1627” in the file (ctrl+f). The object has many attributes, like id, transform, etc… The one we are interested is “d”. This tells us all of the Cartesian points that form the curve. Copy all of the text after “d=” and paste in another file. The shortcut for a new file in Atom is ctrl+n.


tutorial_html_96b7ab9dcaaa77f3.gif

11. Find and replace all spaces by “<font face="STIX">\</font>n”, which is a digital representation of a new line. Make sure that “Use Regex” is enabled.

tutorial_html_7825bcff5a0c2ccb.gif

11. Erase the “m” in the first line and give it a quick check to see if it has a pair of number separated by a comma in all rows. These are (x, y) Cartesian coordinates that draw the curve on the screen. The “m” that we just erased was a instruction for how to interpret the following Cartesian points, that stands for “move”. This means that only absolute point is the first one and all of the subsequent points are relative to the previous point at the row above.

If the instruction is not “m”, we have to be careful about how to interpret the (x, y) coordinates. Other instructions like “l”, which stands for “line”, will also work as “m”. If the first letter is not “m” nor “l” or if you have multiple instructions along the file (letters in other rows other than the first one), go back and do item 5 again. If necessary, <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths">here</a> is a list of other instructions that svg files use to construct paths.


tutorial_html_99d43e4010ba75b7.gif

12. Save the file as data.txt.

13. Now, before going any further, we need to go back to Inkscape and find the exact (x, y) coordinates of the <u>first</u> and the <u>last</u> data point. In this example, it is not clear what are the (x, y) values of the first data point, mostly because of the poor number of ticks in the y and x axes.

There are many ways we can use to find the exact values the data points. Here, I am showing one possible way of how we can do it using <a href="https://en.wikipedia.org/wiki/Cross-multiplication">Cross-multiplication</a> and Inkscape. Firstly, use the Belzier tool to draw lines (hold ctrl to make straight lines and use double click to draw the line). If necessary, there are many of tutorials on the internet on how to use this tool. By paying attetion to the size of these lines we are able to transform between spacial coordinates to the “graph units”. Particularly, in this example (see below), we know that 11.964 mm is equivalent to 0.5, therefore, 18.246 is equivalent to 0.7625. This means that the y coordinate of the first data point is 0.7625.


tutorial_html_50fcfe9dfbaa020.gif

>If we do the same for the x coordinate of the first data point (see below), we will see that 12.706 mm is equivalent to 5, therefore, 2.532 is equivalent to 0.9964. This means that the x coordinate of the first data point is
0.9968.

tutorial_html_68de17876c64bd6d.gif


Finally, if we do the same for the last data point, we will see that its coordinates are roughly (25, 0.0114).

14. Open a spreadsheet software (in this case LibreOffice Calc). Click and drag
data.txt to the spreadsheet and import data using comma as a separator.


tutorial_html_3f5e3d09091e356e.gif

16. It is useful to rearrange the spreadsheet to look something like the image below. Note that, we have the coordinates of the first and last data point
that we found in item 13. Also, we have two values defined as Delta x and Delta y which are the difference between the value of the last and first data points for x and y, respectively. Cell B10 is just “=B6-B2”, while B11 is “=B7-B3”.


tutorial_html_af848403535ca623.gif

17. Cells D2 and E2 are the only ones that have data points with absolute values. The following rows have relative coordinates. We can make all data points absolute by making the first data point (0, 0) in columns F and G and
use the appropriate formula in the following rows (see below).

tutorial_html_3873c096412c4226.gif

18. The data points of columns F and G are in “drawing units” (cm, mm, in, …). By subtracting the value of the last and first data points in these columns we can fill out cells B14 and B15.

tutorial_html_67d924ce936660ae.gif

19. We must then define the calibration factor that will help us go from “drawing units” to “real units”. The calibration factor for the x coordinate is given by “=B10/B14” while the one for y is “=B11/B15”.

tutorial_html_4cc82b6091c9cbfd.gif

20. The final data points can be found by multiplying each data point by the calibration factor and adding the value of the first data point for the x and y
coordinates (See below).


tutorial_html_5ceafd8cd56405f4.gif


21. Done! Columns H and I are the x and y values of the data points. The figure below shows a plot of these columns. Finally, we can export these columns to a text file and use it elsewhere.

tutorial_html_cb14165c020d29d9.gif
