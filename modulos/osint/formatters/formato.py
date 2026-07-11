from .format_api import format_ipwhois, format_ipapi, format_freeipapi,format_ip_api, format_ipinfo
FORMATADORES = {
    "ipwhois": format_ipwhois,
    "ipapi": format_ipapi,
    "ipinfo": format_ipinfo,
    "freeipapi": format_freeipapi,
    "ip_api": format_ip_api
}
