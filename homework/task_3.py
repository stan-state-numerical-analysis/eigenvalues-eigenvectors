# Task: Implement the QR-Algorithm for Finding the Spectrum of a Matrix

# 1. Import numpy with its corresponding alias.



# 2. Define a function qr_decomposition that returns two matrices Q (orthogonal) and R (upper triangular)
# such that A = QR, where A is a square matrix.
#    - Parameters:
#      - A: The square matrix whose QR decomposition is to be computed.



    # 3. Initialize a variable n to be the number of rows (and columns) of A.



    # 4. Initialize U as an all-zero matrix with the same dimensions as A and float data type.



    # 5. Initialize Q as an all-zero matrix with the same dimensions as A and float data type.



    # 6. Initialize R as an all-zero matrix with the same dimensions as A and float data type.



    # 7. Start the Gram-Schmidt process by iterating through each column of A.
    # Use i as the dummy variable in the loop.


        # 8. Set the i-th column of U to the i-th column of A.



        # 9. Iterate through each of the *previous* columns
        # of A. Use j as the dummy variable in the loop.


            # 10. Compute the projection of the i-th column of A onto
            # the j-th column of Q. Call the output proj.



            # 11. Update the i-th column of U to subtract the projection above.



        # 12. Update the i-th column of Q to be the normalized i-th column of U.



    # 13. Compute R.



    # 14. Return the matrices Q and R.



# 15. Define a function qr_algorithm that finds all eigenvalues of a matrix A.
#    - Parameters:
#      - A: The matrix for which you want to find eigenvalues.
#      - num_iter: The number of iterations to run the QR algorithm.



    # 16. Initialize a variable called A_k and set it equal to a copy of A.



    # 17. Loop through the prescribed number of iterations.



        # 18. Use the qr_decomposition function defined above to calculate the QR decomposition of A_k.



        # 19. Update A_k using the matrices R and Q.



    # 20. Initialize the variable eigenvalues and set it to the values on the diagonal of A_k



    # 21. Return the list of eigenvalues.


