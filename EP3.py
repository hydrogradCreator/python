import numpy as np

nome = "Rafaela de Fátima Silva Alexandre"
matricula = 2021031661

def EP_answers(A, B):
    import numpy as np
    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    np.random.seed(1)
    U, Sigma, Sigma_vet, Vt, imgReconst_3, log_Sigma, cumul_Sigma, rmseReconst_3 = [None]*8
    imgReconst_10, rmseReconst_10, imgReconst_100 = [None]*3
    rmseReconst_100, imgReconst_500, rmseReconst_500 = [None]*3
    uso_k_10, uso_k_100, uso_k_500, lim_energ = [None]*4
    B_media, Bm, S, w2, V2, valores_sing, Sigma_vals_sing, Sigma_inv, U2_10, imgs2_10 = [None]*10
    #########################################################################

    ### PARTE 1

    ## 1.1
    ## Insira seu código aqui
  
    U, Sigma_vet, Vt = np.linalg.svd(A)
    
    ## 1.2
    ## Insira seu código aqui
    Sigma = np.diag(Sigma_vet)
    ## 1.3
    ## Insira seu código aqui
    def reconstrucao_aproximada(U, S, Vt,k):

        aprox =  U[:,:k] @ S[:k,:k] @ Vt[:k,:]
        return aprox


    imgReconst_3 = reconstrucao_aproximada(U,Sigma,Vt,3)
    
    ## 1.4
    ## Insira seu código aqui
    log_Sigma = np.log(Sigma_vet)
    cumul_Sigma = np.cumsum(Sigma_vet)
    
    ## 1.5
    ## Insira seu código aqui
    def calcula_RMSE (img_original, img_aprox):
        return np.sqrt(((img_original-img_aprox) ** 2).mean())


    rmseReconst_3 = calcula_RMSE(A, imgReconst_3)
    
    ## 1.6
    ## Insira seu código aqui
    imgReconst_10 = reconstrucao_aproximada(U,Sigma,Vt,10)
    rmseReconst_10 = calcula_RMSE(A, imgReconst_10);
    
    
    imgReconst_100 = reconstrucao_aproximada(U,Sigma,Vt,100)
    rmseReconst_100 = calcula_RMSE(A, imgReconst_100);
    
    imgReconst_500 = reconstrucao_aproximada(U,Sigma,Vt,500)
    rmseReconst_500 = calcula_RMSE(A, imgReconst_500)
    ## 1.7
    ## Insira seu código aqui
    def calcula_qtd_elementos(U, Sigma_vet, Vt):
        return   U.size + Sigma_vet.size + Vt.size


    uso_k_10 = calcula_qtd_elementos(U[:,:10],Sigma_vet[:10],Vt[:10,:])
    uso_k_100 = calcula_qtd_elementos(U[:,:100],Sigma_vet[:100],Vt[:100,:])
    uso_k_500 = calcula_qtd_elementos(U[:,:500],Sigma_vet[:500],Vt[:500,:])
    ## 1.8
    ## Insira seu código aqui
    
    def get_limite(qntd_minima, cumul_Sigma):
          k=0
          while(cumul_Sigma[k]/cumul_Sigma[-1]) < qntd_minima:
            k+=1
          return k
        
    lim_energ = get_limite(0.8,cumul_Sigma)
    ### PARTE 2
    ## Insira seu código aqui

    ## 2.1
    ## Insira seu código aqui
    B_media = np.mean(B, axis=0) #operacoes sobre as linhas
    B_media.size
    
    Bm = B - B_media

    ## 2.2
    ## Insira seu código aqui
    S = Bm.T @ Bm
    
    ## 2.3
    ## Insira seu código aqui
    w2,V2 = np.linalg.eig(S)
    ind = np.argsort(w2)[::-1]
    w2 = w2[ind]
    V2 = V2[:,ind]

    ## 2.4
    ## Insira seu código aqui
    valores_sing = np.sqrt(w2)

    ## 2.5
    ## Insira seu código aqui
    Sigma_vals_sing = np.diag(valores_sing)
    Sigma_vals_sing.shape
    Sigma_inv = np.diag(1/valores_sing)

    ## 2.6
    ## Insira seu código aqui
    U2_10 = Bm[:10,:] @ V2 @  Sigma_inv

    imgs2_10 = reconstrucao_aproximada(U2_10,Sigma_vals_sing,V2.T,200)

    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    answers = {
        "1.1.1" : (U, 'U'),
        "1.1.2" : (Sigma_vet, 'Sigma_vet'),
        "1.1.3" : (Vt, 'Vt'),
        "1.2" : (Sigma, "Sigma"),
        "1.3" : (imgReconst_3, 'imgReconst_3'),
        "1.4.1" : (log_Sigma, 'log_Sigma'),
        "1.4.2" : (cumul_Sigma, 'cumul_Sigma'),
        "1.5" : (rmseReconst_3, 'rmseReconst_3'),
        "1.6.1" : (imgReconst_10, 'imgReconst_10'),
        "1.6.2" : (rmseReconst_10, 'rmseReconst_10'),
        "1.6.3" : (imgReconst_100, 'imgReconst_100'),
        "1.6.4" : (rmseReconst_100, 'rmseReconst_100'),
        "1.6.5" : (imgReconst_500, 'imgReconst_500'),
        "1.6.6" : (rmseReconst_500, 'rmseReconst_500'),
        "1.7.1" : (uso_k_10, 'uso_k_10'),
        "1.7.2" : (uso_k_100, 'uso_k_100'),
        "1.7.3" : (uso_k_500, 'uso_k_500'),
        "1.8" : (lim_energ, 'lim_energ'),
        "2.1.1" : (B_media, 'B_media'),
        "2.1.2" : (Bm, 'Bm'),
        "2.2" : (S, 'S'),
        "2.3.1" : (w2, 'w2'),
        "2.3.2" : (V2, 'V2'),
        "2.4" : (valores_sing, 'valores_sing'),
        "2.5.1" : (Sigma_vals_sing, 'Sigma_vals_sing'),
        "2.5.2" : (Sigma_inv, 'Sigma_inv'),
        "2.6.1" :  (U2_10, 'U2_10'),
        "2.6.2" : (imgs2_10, 'imgs2_10')
    }
    return answers
    ##########################################################################
