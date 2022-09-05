<img src="./images/Archer2_logo.png" width="355" height="100"
align="left"> <img src="./images/epcc_logo.jpg" align="right"
width="133" height="100">

<br /><br /><br /><br /><br />

# Make your Python code 10,000 times faster with parallel numpy!

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<h3>David Henty, EPCC.<br />
Wednesday 7th September 2022, 09:00 - 12:30 BST
</h3>

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

Follow the installation instructions at
[https://github.com/davidhenty/PythonHPCprep/#readme](https://github.com/davidhenty/PythonHPCprep/#readme).

<h3>Timetable (all times are in BST)</h3>

<p><blockquote>Unless otherwise indicated all material is Copyright
&copy; EPCC, The University of Edinburgh, and is only made available
for private study. </blockquote></p>

 * 09:00 - 09:10 : Introduction
 * 09:10 - 09:30 : Traffic Model (lecture)
 * 09:30 - 09:45 : Traffic Model (hands-on)
 * 09:45 - 10:10 : Introduction to Numpy Arrays (lecture)
 * 10:10 - 10:30 : Traffic Model with Numpy (hands-on)
 * 10:30 - 11:00 : Coffee Break
 * 11:00 - 11:30 : Message-Passing Concepts (lecture)
 * 11:30 - 11:40 : Log on to ARCHER2 (hands-on)
 * 11:40 - 12:00 : Basic MPI with mpi4py (lecture)
 * 12:00 - 12:30 : Parallel Traffic Model (hands-on)

<h3>Course material</h3>

Download and unzip
[PythonHPC.zip](https://github.com/EPCCed/PythonHPC/raw/main/PythonHPC.zip)
which includes all the Jupyter notebooks for the exercises on your
laptop - see the directory `notebooks`.

<h3>ARCHER2 exercises</h3>

We are not using Jupyter notebooks on ARCHER2 - follow the instructions below.

* Log on to ARCHER2 using `ssh` - you will have an account in the project `ta083`
* Change directory to `/work` using `cd /work/ta083/ta083/$USER/`
* Copy over the exercises material: `cp /work/ta083/ta083/shared/PythonHPC.zip .`
* Unpack it: `unzip PythonHPC.zip`
* Change directory: `cd PythonHPC/code/`

You will see a number of directories containing C, Fortran and Python
examples in serial, MPI and also OpenMP (although not the latter for
Python). We are only concerned with the Python examples.

* Load the Python environment: `module load cray-python`
* Go to the `P-SER-NP` directory for the numpy version.
* Execute the traffic model: `python traffic.py` - how does the speed
  compare to your laptop?

We should really be running all computational jobs on the compute
nodes which we access by submitting the batch script `archer2.job` (in
fact you cannot run parallel jobs on the login nodes - you have to use
the compute nodes).

* Submit the batch job: `sbatch archer2.job` - this will run the numpy
  code on a single process.

* Output will eventually appear in a file called something like
  `traffic-1234567.out` - you can monitor progress of your jobs using
  `squeue $USER`

* Is the performance on the compute nodes similar to the login nodes?

We will now run the parallel version on ARCHER2. You will see that we
have increased the number of iterations by a factor of 10 - without
this the runtimes become so short that it is difficult to get accurate
performance figures. As a rule of thumb, anything less than a second
is probably too short.

* Submit the batch job: `sbatch archer2.job` - this will run the parallel MPI code
  code on all 128 processors of a single ARCHER2 node.

* What is the performance? How much faster is it than the numpy code
  on a single process? How much faster is it than the original code?

* You can run on 256 or 512 processors by editing `archer2.job` and
  increasing the value of `nodes` to 2 or 4. These jobs may take a
  surprisingly long time to run - this is due to slow startup times
  for parallel Python jobs and not slow performance. At these high
  process counts you may want to increase the number of iterations by
  another factor of 10.

* Did we manage to break the 10,000 times faster barrier?

---

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]


