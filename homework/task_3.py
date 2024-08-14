# Task: Implement the QR-Algorithm for Finding the Spectrum of a Matrix

# 1. Import numpy with its corresponding alias.



# 2. Define a function qr_decomposition that returns two matrices Q (orthogonal) and R (upper triangular)
# such that A = QR, where A is a square matrix.
#    - Parameters:
#      - A: The square matrix whose QR decomposition is to be computed.



    # 3. Initialize a variable n to be the number of rows (and columns) of A.



    # 4. Initialize the Q matrix as an all-zero matrix with the same dimensions as A,
    # and float data type.



    # 5. Initialize the R matrix as an all-zero matrix with the same dimensions as A,
    # and float data type.



    # 6. Start the Gram-Schmidt process by iterating through each column of A.



        # 7. Set the current column of Q, called v, to be the same as the current column of A initially.



        # 8. Iterate through the previous columns of Q to make v orthogonal to them.



            # 9. Update the entry in R using the dot product of the current (previous) column of Q with v.



            # 10. Update v by subtracting its projection onto the current (previous) column of Q.



        # 11. Update the diagonal entry of R to be the norm of v.



        # 12. Update the current column of Q using the normalized version of v.



    # 13. Return the matrices Q and R.



# 14. Define a function qr_algorithm that finds all eigenvalues of a matrix A.
#    - Parameters:
#      - A: The matrix for which you want to find eigenvalues.
#      - num_iter: The number of iterations to run the QR algorithm.



    # 15. Initialize a variable called A_k and set it equal to a copy of A.



    # 16. Loop through the prescribed number of iterations.



        # 17. Use the qr_decomposition function defined above to calculate the QR decomposition of A_k.



        # 18. Update A_k using the matrices R and Q.



    # 19. Initialize the variable eigenvalues and set it to the values on the diagonal of A_k



    # 20. Return the list of eigenvalues.


