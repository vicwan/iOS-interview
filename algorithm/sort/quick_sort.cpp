int partition(int* A, int lo, int hi)
{
    int x = A[lo];
    while(lo < hi)
    {
        while(lo < hi && A[hi] > x)
            hi--;
        if(lo < hi)
        {
            A[lo] = A[hi];
            lo++;
        }

        while(lo < hi && A[lo] <= x)
            lo++;
        if(lo < hi)
        {
            A[hi] = A[lo];
            hi--;
        }
    }
    A[lo] = x;
    return lo;
}

void quick_sort(int* A, int lo, int hi)
{
    if (lo < hi)
    {
        int pivot = partition(A, lo, hi);
        quick_sort(A, lo, pivot);
        quick_sort(A, pivot + 1, hi);
    }
}