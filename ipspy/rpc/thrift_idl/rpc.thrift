namespace py ipspyrpc

service ipspyrpc {
    void ping()
    string version()
    void upload_detail(1:string mac_addr, 2:string ip, 3:string country, 4:string hostname)
}
