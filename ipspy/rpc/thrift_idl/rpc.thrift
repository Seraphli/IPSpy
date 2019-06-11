namespace py ipspyrpc

service ipspyrpc {
    void ping()
    string version()
    void upload_detail(1:string ip, 2:string country, 3:string hostname)
}
