"""MEF_ELINE Test 1 ping."""

# from pythonping import ping
import os
import sys
import subprocess


#
# class Ping():
#
#     flag = ""
#     target = ""
#     count = 0
#     file = "ping_result.txt"
#
#     def __init__(self, target="127.0.0.1", count=4, flag=None):
#         """
#
#         :param target:
#         :param count:
#         :param flag:
#         """
#         self.target = target
#         self.count = int(count)
#         self.flag = flag
#
#     def create_ping_message(self, ping_response=dict):
#
#         index = 0
#         str_response = ""
#
#         while index < self.count:
#
#             if ping_response and (index in
#                                   ping_response.fromkeys() and
#                                   "success" in ping_response.get(index).fromKeys):
#                 if ping_response.get(index).get("success"):
#
#                     str_response += ""
#                     pass
#
#                 else:
#
#                     pass
#
#             index += 1
#             msg = ""
#
#
#
#     def run_ping(self):
#         try:
#
#
#             ping_var = ping(self.target, count=self.count,verbose=True)
#
#             index = 0
#             out = {index: {}}
#
#             for i in ping_var._responses:
#
#                 out.update({index: {"error_message": i.error_message,
#                                     "message_packet.LEN_TO_PAYLOAD": i.message.packet.LEN_TO_PAYLOAD,
#                                     "message_packet_expected_checksum": i.message.packet.expected_checksum,
#                                     "message_packet_header_length": i.message.packet.header_length,
#                                     "message_packet_id": i.message.packet.id,
#                                     "message_packet_is_valid": i.message.packet.is_valid,
#                                     "message_packet_message_code": i.message.packet.message_code,
#                                     "message_packet_message_type": i.message.packet.message_type,
#                                     "message_packet_packet": i.message.packet.packet,
#                                     "message_packet_payload": i.message.packet.payload,
#                                     "message_packet_received_checksum": i.message.packet.received_checksum,
#                                     "message_packet_sequence_number": i.message.packet.sequence_number,
#                                     "message_source": i.message.source, "message_target": i.message.target,
#                                     "success": i.success, "time_elapsed": i.time_elapsed,
#                                     "time_elapsed_ms": i.time_elapsed_ms, "rtt_avg": ping_var.rtt_avg,
#                                     "rtt_avg_ms":ping_var.rtt_avg_ms, "rtt_max": ping_var.rtt_max,
#                                     "rtt_max_ms": ping_var.rtt_max_ms, "rtt_min": ping_var.rtt_min,
#                                     "rtt_min_ms": ping_var.rtt_min_ms}})
#                 index += 1
#
#                 print(out)
#
#             op = None
#
#             if os.path.isfile(self.file):
#                 op = open(self.file, 'a')
#             else:
#                 op = open(self.file, 'w')
#
#             if op:
#                 op.write(out)
#                 op.close()
#         except Exception as e:
#
#             print(e)


class PingCommand():

    file = "ping_result.txt"

    count = '4'

    host = ''

    mode = ''

    cmd = 'ping -c '

    def __init__(self, count=None, host=None, mode=None):
        """

        """

        self.host = host
        self.count = count
        self.mode = mode

    def run_command(self):
        """

        :return:
        """

        # with open(os.devnull, 'w') as DEVNULL:
        #     try:
        #         subprocess.check_call(
        #             ['ping', '-c', '3', '127.0.0.1'],
        #             stdout=DEVNULL,  # suppress output
        #             stderr=DEVNULL
        #         )
        #
        #
        #         is_up = True
        #     except subprocess.CalledProcessError:
        #         is_up = False

        try:
            response = subprocess.check_output(
                ['ping', '-c', self.count, self.host],
                stderr=subprocess.STDOUT,  # get all output
                universal_newlines=True  # return string not bytes
            )

            print(response)


            test1 = str(response).splitlines()
            test2 = list()

            for i in test1:

                test2.append(str(i).split(' '))


            print(test2)

            return response

        except subprocess.CalledProcessError:
            response = None

        # self.cmd += self.count + ' ' + self.host #+ ' ' + self.mode
        #
        # #test = os.system(self.cmd)
        #
        # out = subprocess.Popen(self.cmd)
        #
        # out.wait()
        #
        # # stdout, stderr = out.communicate()
        #
        # str = out.poll()
        #
        # print(str)

    def save_result(self):

        try:

            out = self.run_command()

            op = None

            if os.path.isfile(self.file):
                op = open(self.file, 'a')
            else:
                op = open(self.file, 'w')

            if op:
                op.write(out)
                op.close()
        except Exception as e:

            print(e)


if __name__ == "__main__":

    len = sys.argv.__len__()

    arg_one = None
    arg_two = None
    arg_three = None

    if len > 3:
        arg_one = sys.argv[1]
        arg_two = sys.argv[2]
        arg_three = sys.argv[3]
    else:
        arg_one = sys.argv[1]
        arg_two = sys.argv[2]

    var = PingCommand(arg_one, arg_two, arg_three)

    var.save_result()

    # var = Ping(target=arg_one, count=arg_two, flag=arg_three)
    # var.run_ping()

