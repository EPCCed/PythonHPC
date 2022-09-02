program traffic

  use omp_lib
  use trafficlib

  implicit none

! Set the size of the road

  integer :: ncell = 10240000
  integer :: maxiter, printfreq

  integer :: i, iter, nmove, ncars
  real    :: density

  integer, allocatable, dimension(:) :: newroad, oldroad

  double precision :: tstart, tstop

  maxiter = 1.024e9/ncell
  printfreq = maxiter/10

! Set target density of cars

  density = 0.52

  write(*,*) 'Length of road is ', ncell
  write(*,*) 'Number of iterations is ', maxiter
  write(*,*) 'Target density of cars is ', density

! Spawn a parallel region so we can compute number of threads
! Use master directive to ensure only one thread prints to screen

!$omp parallel
!$omp master
  write(*,*) 'Running on ', omp_get_num_threads(), ' thread(s)'
!$omp end master
!$omp end parallel

! Parallel region ended - now running on a single thread again

! Allocate arrays

  allocate(newroad(0:ncell+1))
  allocate(oldroad(0:ncell+1))

! Initialise road accordingly using random number generator

  do i = 1, ncell
     oldroad(i) = 0
     newroad(i) = 0
  end do

  write(*,*) 'Initialising ...'

  ncars = initroad(oldroad(1), ncell, density, seed)

  write(*,*) '... done'

  write(*,*) 'Actual density of cars is ', float(ncars)/float(ncell)
  write(*,*)

  tstart = gettime()

  do iter = 1, maxiter

     call updatebcs(oldroad, ncell)

     nmove = updateroad(newroad, oldroad, ncell)

! Copy new to old array

!$omp parallel do default(none) shared(ncell, oldroad, newroad)

     do i = 1, ncell

        oldroad(i) = newroad(i)

     end do

     if (mod(iter, printfreq) .eq. 0) then

        write(*,*) 'At iteration ', iter, ' average velocity is ', &
             float(nmove)/float(ncars)
     end if

  end do

  tstop = gettime()

  deallocate(newroad)
  deallocate(oldroad)

  write(*,*)
  write(*,*) 'Finished'
  write(*,*)
  write(*,*) 'Time taken was  ', tstop - tstart, ' seconds'
  write(*,*) 'Update rate was ', &
              1.d-6*float(ncell)*float(maxiter)/(tstop-tstart), ' MCOPs'
  write(*,*)

end program traffic
