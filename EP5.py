nome = "Rafaela de Fátima Silva Alexandre"
matricula = 2021031661

def EP_answers():
    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    import numpy as np
    np.random.seed(1)
    inversa, pseudo_inversa, QR, substituicao, retrosubstituicao, \
    positiva_definida, simetrica, cholesky = [None]*8
    #########################################################################

    ## 1.1
    ## Insira seu código aqui
    def inversa(X,y):
        return np.linalg.inv(X.T @ X) @ X.T @ y

    ## 1.2
    ## Insira seu código aqui
    def pseudo_inversa(X,y):

      U, sigma, V = np.linalg.svd(X, full_matrices=False)
      sigma_inv = np.diag(1/sigma)
      return V.T @ sigma_inv @ U.T @ y
      
    ## 1.3
    ## Insira seu código aqui
    def QR(X,y):
        Q,R = np.linalg.qr(X)
        R_inversa = np.linalg.inv(R)
        b_hat = R_inversa @ Q.T @ y
        return b_hat

    ## 1.4
    ## Insira seu código aqui
    def substituicao(L,b):
        return np.linalg.inv(L) @ b
    
    def retrosubstituicao(Lt,C):
        return np.linalg.inv(Lt) @ C
    
    def positiva_definida(X):
        return np.all(np.linalg.eigvals(X) > 0)
    
    def simetrica(X):
        return np.allclose(X, X.T)
    
    def cholesky(X, y):
        A = X.T @ X
    
        assert positiva_definida(A), 'A matriz "A" não é positiva definida'
        assert simetrica(A), 'A matriz "A" não é simétrica'
    
        L = np.linalg.cholesky(A)
        C = substituicao(L, X.T @ y)
    
        return retrosubstituicao(L.T, C)

    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    answers = {
        "1.1.1" : inversa,
        "1.2" : pseudo_inversa,
        "1.3" : QR,
        "1.4.1" : substituicao,
        "1.4.2" : retrosubstituicao,
        "1.4.3" : positiva_definida,
        "1.4.4" : simetrica,
        "1.4.5" : cholesky
    }
    return answers
    ##########################################################################