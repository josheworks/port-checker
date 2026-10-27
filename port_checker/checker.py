import socket
from port_checker.validators import validate_host


def check_port(host, port, timeout=3):

    if not validate_host(host):
        result = {
            "host": host,
            "port": port,
            "status": "INVALID_HOST",
            "message": "Hostname cannot be empty"
}
        return result

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))

            result = {
                "host":host,
                "port":port,
                "status":"CONNECTED",
                "message":"TCP connected established"
}

        return result

    except ConnectionRefusedError:
        result = {
                "host":host,
                "port":port,
                "status":"REFUSED",
                "message":"Connection Refused"
}

        return result

    except TimeoutError:
        result = {
                "host":host,
                "port":port,
                "status":"TIMEOUT",
                "message":"Connection attempt timed out"
}
        return result

    except socket.gaierror: 
        result = {
                "host":host,
                "port":port,
                "status":"DNS_ERROR",
                "message":"Hostname could not be resolved"
}
        return result

    except OSError as error:
        result= {
            "host":host,
            "port":port,
            "status":"NETWORK_ERROR",
            "message":str(error)
        }
        return result