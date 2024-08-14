# Task: Implement the Power Method and QR Algorithm for Finding the Largest Eigenvalue

# 1. Import numpy with its corresponding alias.



# 2. Define a function power_method that finds the largest eigenvalue and the corresponding eigenvector.
#    - Parameters:
#      - A: The matrix for which you want to find the largest eigenvalue.
#      - b: The initial guess for the eigenvector.
#      - num_iter: The number of iterations to run the power method.



    # 3. Set the numpy random seed value to 13.



    # 4. Initialize a variable called eigenvector and set it equal to a random vector
    # with the correct length.



    # 5. Loop through the prescribed number of iterations.



        # 6. Update eigenvector via the correct matrix multiplication.



        # 7. Update eigenvector so that it is normalized.



    # 8. Compute the Rayleigh quotient to approximate the largest eigenvalue.
    # Call the output eigenvalue.



    # 9. Return the eigenvalue, eigenvector pair.



# 10. Define a function qr_decomposition that returns two matrices Q (orthogonal) and R (upper triangular)
# such that A = QR, where A is a square matrix.
#    - Parameters:
#      - A: The square matrix whose QR decomposition is to be computed.



    # 11. Initialize a variable n to be the number of rows (and columns) of A.



    # 12. Initialize the Q matrix as an all-zero matrix with the same dimensions as A,
    # and float data type.



    # 13. Initialize the R matrix as an all-zero matrix with the same dimensions as A,
    # and float data type.



    # 14. Start the Gram-Schmidt process by iterating through each column of A.



        # 15. Set the current column of Q, called v, to be the same as the current column of A initially.



        # 16. Iterate through the previous columns of Q to make v orthogonal to them.



            # 17. Update the entry in R using the dot product of the current (previous) column of Q with v.



            # 18. Update v by subtracting its projection onto the current (previous) column of Q.



        # 19. Update the diagonal entry of R to be the norm of v.



        # 20. Update the current column of Q using the normalized version of v.



    # 21. Return the matrices Q and R.



# 22. Define a function qr_algorithm that finds all eigenvalues of a matrix A.
#    - Parameters:
#      - A: The matrix for which you want to find eigenvalues.
#      - num_iter: The number of iterations to run the QR algorithm.



    # 23. Initialize a variable called A_k and set it equal to a copy of A.



    # 24. Loop through the prescribed number of iterations.



        # 25. Use the qr_decomposition function defined above to calculate the QR decomposition of A_k.



        # 26. Update A_k using the matrices R and Q.



    # 27. Initialize the variable eigenvalues and set it to the values on the diagonal of A_k



    # 28. Return the list of eigenvalues.


