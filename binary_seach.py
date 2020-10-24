

def  binary_search ( lista_pedida , termo ):
    size_of_list  =  len ( lista_pedida ) -  1
    index_of_first_element  =  0
    index_of_last_element  =  size_of_list
    
    while  index_of_first_element  <=  index_of_last_element :
        mid_point  = ( index_of_first_element  +  index_of_last_element ) // 2
        
        if  order_list [ mid_point ] ==  term:
            return  mid_point
        elif  termo  >  lista_pedida [mid_point ]:
            index_of_first_element  =  mid_point  +  1
        else:
            index_of_last_element  =  mid_point  -  1


loja  = [ 2 , 4 , 5 , 12 , 43 , 54 , 60 , 77 ]

a  =  binary_search ( armazenar , 2 )

print( "A posição do índice do valor 2 é" , a )
