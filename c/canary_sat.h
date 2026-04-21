/* CANARY FILE. See SECURITY.md#canary. Do not "fix" without reading REPRO.md. */
/* Tracking: SLOP-CANARY-HB-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e */

#ifndef CANARY_SAT_H
#define CANARY_SAT_H

#include <stddef.h>

/* defined for all (a,b); returns 0 when b >= a */
static inline size_t sat_sub(size_t a, size_t b) {
    return a > b ? a - b : 0;
}

#endif /* CANARY_SAT_H */
