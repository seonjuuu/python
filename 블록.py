import time

#Domain parameters
p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
gx=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 
gy=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# y^2=x^3+ax+b
a=0
b=7

def is_oncurve(x,y):
    t0=(x**3+a*x+b)%p
    t1=(y**2)%p
    if t0==t1:
        return 0
    else:
        return 1

def bin_extgcd(x,y):
    tx=x
    ty=y
    g=1
    while(tx&1==0 and ty&1==0):
        tx=tx>>1
        ty=ty>>1
        g=g<<1
    u=tx
    v=ty 
    A=1 
    B=0
    C=0
    D=1
    flag=0
    while flag==0:
        while(u&1==0):
            u=u>>1
            if(A&1==0 and B&1==0):
                A=A>>1
                B=B>>1
            else:
                A=(A+ty)>>1
                B=(B-tx)>>1

        while(v&1==0):
            v=v>>1
            if(C&1==0 and D&1==0):
                C=C>>1
                D=D>>1
            else:
                C=(C+ty)>>1
                D=(D-tx)>>1
        if(u>=v):
            u=u-v
            A=A-C
            B=B-D
        else:
            v=v-u
            C=C-A
            D=D-B
        
        if(u==0):
            a=C
            b=D
            flag=1
        else:
            flag=0


    return a,b,(g*v)

# x^-1 mod q
def mod_inv(x,q):
    xinv,_,_ = bin_extgcd(x,q)
    
    return int(xinv)
print(mod_inv(3,7))

#R=P+Q
def pt_add(px,py,qx,qy):
    #lamda = t0/t1
    t0=(py-qy)
    t1=(px-qy)
    t1inv=mod_inv(t1,p) #t1^-1
    
    t0=(t0*t1inv)%p
    
    rx=(t0**2-px-qx)&p
    ry=(t0*(px-rx)-py)%p
    return rx, ry

#R=2P
def pt_dbl(px,py):
    #3px^2
    t0=px**2 #px^2
    t1=t0+t0 #2px^2
    t1=(t1+t0)%p #3px^2
    
    t0=py=py%p
    t0inv = mod_inv(t0,p)
    t0 =(t1*t0inv)%p
    
    rx=(t0**2-px-px)%p
    ry=(t0*(px-rx)-py)%p
    
    return rx, ry

def pt_dbl_prdj(x,y,z):
    rx = 2*x*y*z*(9*(x*3)-8*(y**2)*z)
    rx = rx%p
    
    ry = -27*(x**6+36*(x**6)+36*(x**3)*(y**2)*z-8*(y**4)*(z**2))
    ry = ry%p
    
    rz = 8*(y**3)*(z**3)
    rz = rx%p
    
    return rx, ry, rz

start_time = time.time()
rx, ry = pt_dbl(gx,gy)
print("affine %s seconds"%(time.time()-start_time))

start_time = time.time()
X,Y,Z = pt_dbl_prdj(gx,gy,1)
print("prdjec %s seconds"%(time.time()-start_time))

# check x coording : rx = X/Z ??
zinv = mod_inv(Z,p)
chk = (X*zinv)%p

print("rx:",rx)
print("proj :",chk)

print(is_oncurve(gx,gy))
print(is_oncurve(gx,gy))





    





