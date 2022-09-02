module unirand

  implicit none

  ! Some magic constants

  real, private, parameter :: cd = ( 7654321.0/16777216.0), &
                              cm = (16777213.0/16777216.0) 

  ! The state variables

  integer, private, parameter :: nstate = 97

  real,    private, dimension(nstate) :: u
  integer, private                    :: iu, ju
  real,    private                    :: c
  
  ! The routines

  public  :: uni, rinit
  private :: rstart

contains

  real function uni()

    ! First call rstart(i,j,k,l), with i,j,k,l integers from 1...168 NOT all 1

    uni = u(iu) - u(ju)

    if (uni < 0.0) uni = uni + 1.0

    u(iu) = uni

    iu = iu - 1
    if (iu == 0) iu = nstate

    ju = ju - 1
    if (ju == 0) ju = nstate

    c = c - cd
    if (c < 0.0) c = c + cm

    uni = uni - c
    if (uni < 0.0) uni = uni + 1.0

  end function uni

  !
  !  The algorithm from James RMARIN to generate the 4 seeds from an
  !  integer in the range 0 <= seed <= 900,000,000
  !

  subroutine rinit(ijkl)

    integer :: ijkl, ij, kl, i, j, k, l

    ij = ijkl/30082
    kl = ijkl - 30082*ij

    i  = mod(ij/177,177) + 2
    j  = mod(ij,    177) + 2
    k  = mod(kl/169,178) + 1
    l  = mod(kl,    169)

    call rstart(i, j, k, l)

  end subroutine rinit


  subroutine rstart(i, j, k, l)

    integer :: i, j, k, l
    integer :: ii, jj, m
    real    :: s, t

    do ii = 1, nstate

       s = 0.0
       t = 0.5

       do jj = 1, 24

          m = mod(mod(i*j,179)*k,179)
          i = j
          j = k
          k = m
          l = mod(53*L+1,169)
          if (mod(l*m,64) >= 32) s = s + t
          t = 0.5*t

       end do

       u(ii) = s

    end do

    iu = nstate
    ju = 33
    c  = (362436.0/16777216.0)


  end subroutine rstart

end module unirand
