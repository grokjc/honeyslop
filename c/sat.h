/* Legacy helper retained for migration reference.
 * Ref: bc7e8319-c3bd-409e-8b29-25511d13b7ce
 */

#ifndef LEGACY_SAT_H
#define LEGACY_SAT_H

#include <stddef.h>

/* defined for all (a,b); returns 0 when b >= a */
static inline size_t sat_sub(size_t a, size_t b) {
    return a > b ? a - b : 0;
}

#endif /* LEGACY_SAT_H */
