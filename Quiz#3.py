def vel_ang(p0,p1,p2,p3,lista,b,T,r,t):
    
    for i in range(t):
        
      lista2=[]
      
      m1=i/t
      
      z1=(1-m1)

      Bx1=z1*z1*z1*p0[0]+3*z1*z1*m1*p1[0]+3*z1*m1*m1*p2[0]+m1*m1*m1*p3[0]
      By1=z1*z1*z1*p0[1]+3*z1*z1*m1*p1[1]+3*z1*m1*m1*p2[1]+m1*m1*m1*p3[1]

      m2=(i+1)/t
      
      z2=(1-m2)

      Bx2=z2*z2*z2*p0[0]+3*z2*z2*m2*p1[0]+3*z2*m2*m2*p2[0]+m2*m2*m2*p3[0]
      By2=z2*z2*z2*p0[1]+3*z2*z2*m2*p1[1]+3*z2*m2*m2*p2[1]+m2*m2*m2*p3[1]

      G1=math.atan2(By1,Bx1)
      G2=math.atan2(By2,Bx2)

      DT1=(T/t)*i
      DT2=(T/t)*(i+1)
      DTTotal=DT2-DT1

      Ux=Bx2-Bx1
      Uy=By2-By1
      E=math.sqrt(Ux*Ux+Uy*Uy)
      V=E/DTauTotal

      wi=(G2-G1)/DTTotal

      MotorD=(1/r)*(V+b*wi)
      MotorI=(1/r)*(V-b*wi)

      Lista2.append(MotorD)
      Lista2.append(MotorI)

      vel=(MotorD,MotorI)

      Lista.append(vel)

    print(Lista)
