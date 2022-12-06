
def find_marker(data, marker_length):
    for index in xrange(len(datastream)):
        quartet = datastream[index:index + marker_length]
        # print 'Quartet {}: {}'.format(index + 1, quartet)
        unique = 0
        for character in quartet:
            if quartet.count(character) > 1:
                # print '{} exists.'.format(character)
                break
            else:
                unique += 1
        if unique == marker_length:
            break
    return index + marker_length

if __name__ == '__main__':
    datastream = open('input06.txt', 'rb').readline().strip()
    start_of_packet_marker_length = 4
    start_of_message_marker_length = 14

    print 'Datastream:', datastream

    print 'start-of-packet marker:', find_marker(datastream, start_of_packet_marker_length)
    print 'start-of-message marker:', find_marker(datastream, start_of_message_marker_length)
