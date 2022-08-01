<img src="./images/Archer2_logo.png" width="355" height="100"
align="left"> <img src="./images/epcc_logo.jpg" align="right"
width="133" height="100">

<br /><br /><br /><br /><br />

# Make your Python code 10,000 times faster with parallel numpy!

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<h3>David Henty EPCC: Tuesday 23rd August 2022, 09:00 - 12:30 BST
online</h3>

Python is widely used in scientific research for tasks such as data
processing, analysis and visualisation. However, it is not yet widely
used for large-scale modelling and simulation on High Performance
Computer (HPC) architectures due to issues with performance – Python
is primarily designed for ease of use and flexibility, not for
speed. For example, a C program naively translated in to Python can
often be over 100 times slower. However, there are techniques that can
be used to dramatically increase the speed of Python programs such as
fast array processing using numpy, parallelisation using MPI
message-passing and running on HPC systems.

In this hands-on workshop we will illustrate these techniques in
practice by applying them to a toy application which simulates traffic
flow using a simple cellular automaton model. Having developed and
tested the program on your own laptop, we will then move to the UK
National Supercomputer ARCHER2 which has in excess of 750,000
CPU-cores. With a combination of numpy and mpi4py we will aim for a
performance increase of more than a factor of 10,000 compared to the
original program.

As much of the programming as possible will be done using Jupyter
Notebooks, but we will run on ARCHER2 via the standard Slurm batch
scheduling system. Although attendees will be encouraged to write
their own code, full solutions will be provided for all exercises. The
main aim is to illustrate the potential power of supercomputer systems
to new users, and to demystify HPC and parallel programming.

<h3>Pre-requisites</h3>

The course assumes a basic understanding of Python programming. You
will also need to be able to run a Jupyter notebook on your own laptop
-- follow the installation instructions at
[https://jupyter.org/install](https://jupyter.org/install).

<h3>Requirements</h3>

Participants must bring a laptop with a Mac, Linux, or Windows
operating system (not a tablet, Chromebook, etc.) that they have
administrative privileges on.

They are also required to abide by the [ARCHER2 Code of Conduct](https://www.archer2.ac.uk/about/policies/code-of-conduct.html).

<h3>Timetable (all times are in BST, GMT+1)</h3>

<p><blockquote>This is still a draft course page and the material
below comes from a previous run of this course. It will be updated for
this run, but is made available here for reference.</blockquote></p>

<p><blockquote>Unless otherwise indicated all material is Copyright
&copy; EPCC, The University of Edinburgh, and is only made available
for private study. </blockquote></p>

<h4>Tuesday 11th January</h4>

 * 09:30 - 10:15 : <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/slides/Parallel-IO-1.pdf">Challenges of Parallel IO</a>
 * 10:15 - 10:45 : <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/slides/Parallel-IO-2.pdf">Lustre file system on ARCHER2</a>
 * 10:45 - 11:00 : Practical: Basic IO performance
 * 11:00 - 11:30 : Break
 * 11:30 - 12:00 : Practical: Basic IO performance (cont)
 * 12:00 - 12:45 : <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/slides/Parallel-IO-3.pdf">Overview of MPI-IO</a>
 * 12:45 - 13:00 : Practical: MPI-IO performance
 * 13:00 - 14:00 : Lunch
 * 14:00 - 14:30 : <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/slides/Parallel-IO-4.pdf">Configuring the Lustre filesystem</a>
 * 14:30 - 15:00 : Practical: MPI-IO performance (cont)
 * 15:00 - 15:30 : <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/slides/Parallel-IO-5.pdf">Higher-level parallel IO libraries</a>
 * 15:30 - 16:00 : Break
 * 16:00 - 16:30 : Q&A / Finish exercises
 * 16:30         : CLOSE

<h3>Exercise Material</h3>

<p><blockquote>Unless otherwise indicated all material is Copyright
&copy; EPCC, The University of Edinburgh, and is only made available
for private study. </blockquote></p>

Here is the <a href="https://github.com/EPCCed/archer2-parallelIO-2022-01-11/raw/main/exercises/benchio-archer2.pdf">parallel IO exercise sheet.</a>. As explained in the sheet, source code and instructions for the IO benchmark can be found at <a href="https://github.com/davidhenty/benchio">https://github.com/davidhenty/benchio/.</a>

---

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

