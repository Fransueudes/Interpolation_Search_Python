def  próximo_mid ( input_list , lower_bound_index , upper_bound_index , search_value ):
    return  lower_bound_index  + (( upper_bound_index  -  lower_bound_index ) // ( input_list [ upper_bound_index ] -  input_list [ lower_bound_index ])) * ( search_value  -  input_list [ lower_bound_index ])

def  interpolation_search ( lista_pedida , termo ):
    size_of_list  =  len ( lista_pedida ) -  1
    index_of_first_element  =  0
    index_of_last_element  =  size_of_list
    while  index_of_first_element  <=  index_of_last_element :
        ponto médio  =  meio_próximo ( lista_ordenada , índice_do_primeiro_elemento , índice_do_último_elemento , termo )
        if  mid_point  >  index_of_last_element  ou  mid_point  <  index_of_first_element :
            return  nenhum
        elif  order_list [ mid_point ] ==  term :
            return  mid_point
        elif  termo  >  lista_pedida [ponto médio ]:
            index_of_first_element  =  mid_point  +  1
        else :
            index_of_last_element  =  mid_point  -  1



loja  = [ 2 , 4 , 5 , 12 , 43 , 54 , 60 , 77 ]
a  =  interpolation_search ( armazenar , 2 )
imprimir ( "A posição do índice do valor 2 é" , a )