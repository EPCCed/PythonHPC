program traffic

  use trafficlib

  implicit none

! Set the size of the road

  integer :: ncell = 10240000
  integer :: maxiter, printfreq

  integer :: i, iter, nmove, ncars
  real    :: density

  integer, allocatable, dimension(:) :: newroad, oldroad

  double precision :: tstart, tstop

  maxiter = 1.024e9/float(ncell)
  printfreq = maxiter/10

! Set target density of cars

  density = 0.52

  write(*,*) 'Length of road is ', ncell
  write(*,*) 'Number of iterations is ', maxiter
  write(*,*) 'Target density of cars is ', density

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
