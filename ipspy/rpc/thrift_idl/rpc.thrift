namespace py ipspyrpc

service ipspyrpc {
    void ping()
    string version()
    void upload_detail(1:string country, 2:string ip)
}
