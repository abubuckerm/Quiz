Pr <- function  (C,F,y,n) #Give inputs in PR())
  {
  v <- c(1:n) #vector(time unit is in half years)
  P = (sum(C*exp(-y*v))) + (F*exp(-y[n]*n)) #Price of Bond Formula
  return(P)     
}

#input 
a <- c(0.06,0.09,0.08,0.7) #taking values for only 4 half years, and a[] the value of interest(efeective half yearly interest rate) at that halfyear
Pr(8000, 10000, a, 4) #input for the set parameter c,f,y,n

