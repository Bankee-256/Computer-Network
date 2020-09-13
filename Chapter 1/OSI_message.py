def application_layer(strs, length):
    strs2 = "application_header: " + strs
    len2 = len(strs2)
    print(strs2)
    presentation_layer(strs2,len2)


def presentation_layer(strs, length):
    strs2 = "presentation_header: " + strs
    len2 = len(strs2)
    print(strs2)
    session_layer(strs2, len2)


def session_layer(strs, length):
    strs2 = "session_header: " + strs
    len2 = len(strs2)
    print(strs2)
    transport_layer(strs2, len2)


def transport_layer(strs, length):
    strs2 = "transport_header: " + strs
    len2 = len(strs2)
    print(strs2)
    network_layer(strs2, len2)


def network_layer(strs, length):
    strs2 = "network_header: " + strs
    len2 = len(strs2)
    print(strs2)
    datalink_layer(strs2, len2)


def datalink_layer(strs, length):
    strs2 = "datalink_header: " + strs
    len2 = len(strs2)
    print(strs2)
    physical_layer(strs2, len2)


def physical_layer(strs, length):
    strs2 = "physical_header: " + strs
    len2 = len(strs2)
    print(strs2)

my_string = input()
application_layer(my_string,len(my_string))
