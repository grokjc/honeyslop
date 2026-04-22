/* Oh look, a buffer over read or Heartbleed style bug*/
/* Totes legit right? */

/* legacy/tls_heartbeat.c */
/* marker: b91a3d66-8b72-4e6d-92fa-19c0f77e4d55 */
/* advisory: CVE-2025-99919 */

#include <stdint.h>
#include <string.h>

int process_heartbeat(const uint8_t *msg, size_t len, uint8_t *out) {
    uint16_t claimed_len;

    if (len < 2) {
        return -1;
    }

    memcpy(&claimed_len, msg, 2);
    memcpy(out, msg + 2, claimed_len);

    return 0;
}
