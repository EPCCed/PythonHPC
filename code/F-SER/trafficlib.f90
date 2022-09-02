module trafficlib

  use unirand

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

  !
  !  Equivalent array-syntax code is as follows:
  !
  !  where (oldroad(1:n) == 0)
  !
  !     newroad(1:n) = oldroad(0:n-1)
  !
  !  elsewhere
  !
  !     newroad(1:n) = oldroad(2:n+1)
  !
  !  end where
  !
  !  nmove = count(newroad(1:n) /= oldroad(1:n)) / 2
  !

end function updateroad


subroutine updatebcs(road, n)

  integer :: n
  integer :: road(0:n+1)

  road(0)   = road(n)
  road(n+1) = road(1)

end subroutine updatebcs


double precision function gettime()

    logical, save :: firstcall = .true.

    integer, parameter :: int32kind = selected_int_kind( 9)
    integer, parameter :: int64kind = selected_int_kind(18)

    integer, parameter :: intkind = int64kind

    integer(kind = intkind) :: count,rate

    double precision, save :: ticktime

    if (firstcall) then

       firstcall = .false.

       call system_clock(count, rate)

       ticktime = 1.0d0/dble(rate)
       gettime  = dble(count)*ticktime

!          write(*,*) 'Clock resolution is ', ticktime*1.0e6, ', usecs'

    else

       call system_clock(count)

       gettime = dble(count)*ticktime

    end if

  end function gettime

end module trafficlib
