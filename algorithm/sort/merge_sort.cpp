void merge(int* A, int lo, int mi, int hi)
{
    int i = lo;
    int m = mi;
    int j = mi + 1;
    int n = hi;
    int k = 0;
    int* tmp = new int[hi - lo + 1];

    while(i <= m && j <= n)
    {
        if(i < j)
        {
            tmp[k++] = A[i++];
        }else
        {
            tmp[k++] = A[j++];   
        }
    }

    while(i <= m)
    {
        tmp[k++] = A[i++];
    }
    while(j <= n)
    {
        tmp[k++] = A[j++];
    }

    i = lo;
    k = 0;
    while(i <= n)
    {
        A[i++] = tmp[k++];
    }
}

void merge_sort(int* A, int lo, int hi)
{
    if(lo < hi)
    {
        int mi = (lo + hi) / 2;
        merge_sort(A, lo, mi);
        merge_sort(A, mi + 1, hi);
        merge(A, lo, mi, hi);
    }
}