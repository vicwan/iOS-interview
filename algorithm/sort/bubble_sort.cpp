
/***************** fast ******************/

bool bubble_scan(int* A, int lo, int hi) 
{
    bool sorted = true;
    while(++lo < hi) 
    {
        if (A[lo - 1] < A[lo]) 
        {
            swap(A[lo - 1], A[lo]);
            sorted = false;
        }
    }
    return sorted;
}

void bubble_sort_fast(int* A, int lo, int hi)
{
    while(!bubble_scan(A, lo, hi))
        hi--;
}

/***************** fastest ******************/

int bubble_scan_fastest(int* A, int lo, int hi)
{
    int last = lo;
    while(++lo < hi) 
    {
        if (A[lo - 1] < A[lo]) 
        {
            swap(A[lo - 1], A[lo]);
            last = lo;
        }
    }
    return lo;
}

void bubble_sort_fastest(int* A, int lo, int hi)
{
    while(lo < (hi = bubble_scan_fastest(A, lo, hi)))
}