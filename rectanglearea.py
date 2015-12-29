def computeArea(A,B,C,D,E,F,G,H):
	a=0;b=0
	if A<=E<C<=G: a=C-E
	elif E<=A<C<=G: a=C-A
	elif E<=A<G<=C: a=G-A
	elif A<=E<G<=C: a=G-E
	else : sumb=0
	if F<=B<D<=H: b=D-B
	elif B<=F<H<=D: b=H-F
	elif B<=F<D<=H: b=D-F
	elif F<=B<H<=D: b=H-B
	else : sumb=0
	sumb=a*b
	suma=(C-A)*(D-B)+(G-E)*(H-F)
	return suma-sumb