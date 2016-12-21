#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.sparse.linalg.eigs.html
import scipy.sparse as sparse
id = np.eye(13)
vals, vecs = sparse.linalg.eigsh(id, k=6)
vals

vecs.shape
