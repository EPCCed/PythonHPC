module trafficlib

  use unirand
  use omp_lib

  implicit none

  integer, parameter :: seed = 5743

contains

integer function initroad(road, n, density, seedval)

  integer :: n, seedval
  integer :: road(n)
  real    :: density
  
  integer :: i, ncar
  real    :: rng

  call rinit(seedval)

  ncar = 0

  do i = 1, n

     rng = uni()

     if (rng .lt. density) then

        road(i) = 1

     else

        road(i) = 0

     end if

     ncar = ncar + road(i)
    
  end do

  initroad = ncar

end function initroad


integer function updateroad(newroad, oldroad, n)

  integer :: n
  integer :: newroad(0:n+1), oldroad(0:n+1)

  integer :: i, nmove

  nmove = 0

!$omp parallel do default(none) shared(n, oldroad, newroad) reduction(+:nmove)

  do i = 1, n

     if (oldroad(i) .eq. 1) then

        if (oldroad(i+1) .eq. 1) then

           newroad(i) = 1
           
        else

           newroad(i) = 0
           nmove = nmove + 1

        end if

     else

        if (oldroad(i-1) .eq. 1) then

           newroad(i) = 1

        else

           newroad(i) = 0
           
        end if

     end if

  end do

  updateroad = nmove

end function updateroad


subroutine updatebcs(road, n)

  integer :: n
  integer :: road(0:n+1)

  road(0)   = road(n)
  road(n+1) = road(1)

end subroutine updatebcs

double precision function gettime()

  gettime = omp_get_wtime()

end function gettime

end module trafficlib
