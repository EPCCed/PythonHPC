#include <stdlib.h>
#include <stdio.h>

#include "traffic.h"

int main(int argc, char **argv)
{
  // Set the size of the road

  int ncell = 10240000;

  int *oldroad, *newroad;

  int i, iter, nmove, ncars;
  int maxiter, printfreq; 

  float density; 

  double tstart, tstop;

  oldroad = (int *) malloc((ncell+2)*sizeof(int));
  newroad = (int *) malloc((ncell+2)*sizeof(int));

  maxiter = 1.024e9/((double) ncell);
  printfreq = maxiter/10;

  // Set target density of cars

  density = 0.52;

  printf("Length of road is %d\n", ncell);
  printf("Number of iterations is %d \n", maxiter);
  printf("Target density of cars is %f \n", density);

  // Initialise road accordingly using random number generator

  for (i=1; i <= ncell; i++)
    {
      oldroad[i] = 0;
      newroad[i] = 0;
    }

  printf("Initialising road ...\n");
  
  ncars = initroad(&oldroad[1], ncell, density, SEED);

  printf("...done\n");

  printf("Actual density of cars is %f\n\n", (float) ncars / (float) ncell);

  tstart = gettime();

  for (iter=1; iter<=maxiter; iter++)
    { 
      updatebcs(oldroad, ncell);

      // Apply CA rules to all cells

      nmove = updateroad(newroad, oldroad, ncell);
      
      // Copy new to old array

      for (i=1; i<=ncell; i++)
	{
	  oldroad[i] = newroad[i]; 
	}

      if (iter%printfreq == 0)
	{
	  printf("At iteration %d average velocity is %f \n",
		 iter, (float) nmove / (float) ncars);
	} 
    }

  tstop = gettime();

  free(oldroad);
  free(newroad);
  
  printf("\nFinished\n");
  printf("\nTime taken was  %f seconds\n", tstop-tstart);
  printf("Update rate was %f MCOPs\n\n", \
	 1.e-6*((double) ncell)*((double) maxiter)/(tstop-tstart));
}
