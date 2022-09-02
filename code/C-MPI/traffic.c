#include <stdlib.h>
#include <stdio.h>

#include <mpi.h>

#include "traffic.h"

int main(int argc, char **argv)
{
  // Set the size of the road

  int ncell = 10240000;

  int *oldroad, *newroad, *bigroad;

  int i, iter, nmove, nmovelocal, ncars;
  int maxiter, printfreq; 

  float density; 

  double tstart, tstop;

  MPI_Status status;
  int rank, size, nlocal, rankup, rankdown;

  maxiter = 1.024e9/((double) ncell);
  printfreq = maxiter/10; 

  // Set target density of cars

  density = 0.52;

  // Start MPI

  MPI_Init(NULL, NULL);  

  // Find size and rank

  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  if (rank == 0)
    {
      printf("Running message-passing traffic model\n");
      printf("\nLength of road is %d\n", ncell);
      printf("Number of iterations is %d \n", maxiter);
      printf("Target density of cars is %f \n", density);
      printf("Running on %d processes\n", size);
    }

  nlocal = ncell/size;

  oldroad = (int *) malloc((nlocal+2)*sizeof(int));
  newroad = (int *) malloc((nlocal+2)*sizeof(int));

  for (i=1; i <= nlocal; i++)
    {
      oldroad[i] = 0;
      newroad[i] = 0;
    }

  if (rank == 0)
    {
      bigroad = (int *) malloc(ncell*sizeof(int));

      // Initialise road accordingly using random number generator

      printf("Initialising road ...\n");
  
      ncars = initroad(bigroad, ncell, density, SEED);

      printf("...done\n");
      printf("Actual density is %f\n", (float) ncars / (float) ncell);
      printf("Scattering data ...\n");
    }

  MPI_Scatter(bigroad,     nlocal, MPI_INT,
	      &oldroad[1], nlocal, MPI_INT,
	      0, MPI_COMM_WORLD);

  if (rank == 0)
    {
      printf("... done\n\n");
    }

  // Compute neighbours

  rankup   = (rank + 1) % size;
  rankdown = (rank + size - 1) % size;

  MPI_Barrier(MPI_COMM_WORLD);

  tstart = MPI_Wtime();

  for (iter=1; iter<=maxiter; iter++)
    { 

      // Implement halo swaps which now includes boundary conditions

      MPI_Sendrecv(&oldroad[nlocal], 1, MPI_INT, rankup, 1,
		   &oldroad[0],      1, MPI_INT, rankdown, 1,
		   MPI_COMM_WORLD, &status);

      MPI_Sendrecv(&oldroad[1],        1, MPI_INT, rankdown, 1,
		   &oldroad[nlocal+1], 1, MPI_INT, rankup, 1,
		   MPI_COMM_WORLD, &status);

      // Apply CA rules to all cells

      nmovelocal = updateroad(newroad, oldroad, nlocal);

      // Globally sum the value

      MPI_Allreduce(&nmovelocal, &nmove, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

      // Copy new to old array

      for (i=1; i<=nlocal; i++)
	{
	  oldroad[i] = newroad[i]; 
	}

      if (iter%printfreq == 0)
	{
	  if (rank == 0)
	    {
	      printf("At iteration %d average velocity is %f \n",
		     iter, (float) nmove / (float) ncars);
	    }
	} 
    }

  MPI_Barrier(MPI_COMM_WORLD);

  tstop = MPI_Wtime();

  free(oldroad);
  free(newroad);

  if (rank == 0)
    {
      free(bigroad);

      printf("\nFinished\n");
      printf("\nTime taken was  %f seconds\n", tstop-tstart);
      printf("Update rate was %f MCOPs\n\n", \
      1.e-6*((double) ncell)*((double) maxiter)/(tstop-tstart));
    }

  // Finish

  MPI_Finalize();
}
