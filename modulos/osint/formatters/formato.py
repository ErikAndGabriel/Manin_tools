from modulos.osint.formatters.formate_api import format_ipwhois, format_ipapi, format_freeipapi,format_ip_api, format_ipinfo, format_cepaberto, format_apicep, format_brasilapi, format_viacep
FORMATADORES = {
    "ipwhois": format_ipwhois,
    "ipapi": format_ipapi,
    "ipinfo": format_ipinfo,
    "freeipapi": format_freeipapi,
    "ip_api": format_ip_api
}

FORMATADORES_CEP = {
    "viacep": format_viacep,
    "brasilapi": format_brasilapi,
    "apicep": format_apicep,
    "api_cep": format_apicep
}
