class Matrix:
    def setdata(self, m, n):
        self.matrix = [n * [0] for i in range(m)]
        
    def sumMatrix(self, other):
        
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print("두 행렬의 크기가 다릅니다.")
            return None
                
        # 결과 행렬을 저장할 리스트 생성
        matR = [len(self.matrix[0]) * [0] for i in range(len(self.matrix))]
        
        for i in range(len(matR)):  # i: 행번호
            for j in range(len(matR[i])):  # j: 열 번호
                matR[i][j] = self.matrix[i][j] + other.matrix[i][j]

        # 결과 행렬 반환
        return matR
    
    def subMatrix(self, other):
        
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print("두 행렬의 크기가 다릅니다.")
            return None
                
        # 결과 행렬을 저장할 리스트 생성
        matR = [len(self.matrix[0]) * [0] for i in range(len(self.matrix))]
        
        for i in range(len(matR)):  # i: 행번호
            for j in range(len(matR[i])):  # j: 열 번호
                matR[i][j] = self.matrix[i][j] - other.matrix[i][j]

        # 결과 행렬 반환
        return matR
    
    def scalarMatrix(self, k):
        
                
        # 결과 행렬을 저장할 리스트 생성
        matR = [len(self.matrix[0]) * [0] for i in range(len(self.matrix))]
        
        for i in range(len(matR)):  # i: 행번호
            for j in range(len(matR[i])):  # j: 열 번호
                matR[i][j] = self.matrix[i][j] * k

        # 결과 행렬 반환
        return matR
    
    def productMatrix(self, other):
    
        # m by n 수만큼 0으로 채워진 리스트 생성
        matR = [ len(other.matrix[0])*[0] for i in range (len(self.matrix)) ]

        
        for i in range (len(matR) ): # i: 행번호
            for j in range ( len(matR[i]) ): #j: 열 번호
                for k in range ( len(self.matrix[i] ) ):

                    matR[i][j] = self.matrix[i][k] * other.matrix[k][j]

        #결과 행렬
        return matR
    
def printMatrix(C):
    if C:
        for row in C:

            print(row)
    
# 테스트를 위한 예제 코드
A = Matrix()
A.setdata(2, 2)
A.matrix = [[2, 1], [5, 3]]

B = Matrix()
B.setdata(2, 2)
B.matrix = [[-1, 4], [1, 2]]
    
C = A.sumMatrix(B)  # A와 B를 더한 결과 Matrix 객체를 C에 저장
printMatrix(C)

C = A.subMatrix(B)  # A와 B를 더한 결과 Matrix 객체를 C에 저장
printMatrix(C)

C = A.scalarMatrix(3)  
printMatrix(C)

C = A.productMatrix(B)  
printMatrix(C)



