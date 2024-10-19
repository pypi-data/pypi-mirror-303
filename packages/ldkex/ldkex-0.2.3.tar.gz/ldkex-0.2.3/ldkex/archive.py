from ldkex.utils import read_int, read_long, read_double, read_pointer, read_string, read_boolean, read_fully


class NodeEntry:
    def __init__(self, file):
        self.position = read_long(file)
        self.uid = read_int(file)


class NodeAdditionalData:
    def __init__(self, file, offset):
        file.seek(offset)
        self.magic_number = read_int(file)
        if self.magic_number != 0x00205555:
            print(f"Node data magic is wrong on offset {offset}")
        self.main_data_size = read_long(file)
        self.data_additional_block_pointer = read_pointer(file)
        self.bytes = read_fully(file, self.main_data_size)


class DataNode:
    TYPE_MAP = {
        0x65: "wpt",
        0x66: "set",
        0x67: "rte",
        0x68: "trk",
        0x69: "are"
    }

    def __init__(self, file, entry, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.node_uuid = entry.uid
        file.seek(entry.position)
        self.magic_number = read_int(file)
        self.flags = read_int(file)
        self.total_size = read_long(file)
        self.main_data_size = read_long(file)
        self.data_additional_block_pointer = read_pointer(file)
        self.bytes = read_fully(file, self.main_data_size)
        self.file_type = self.TYPE_MAP.get(self.bytes[0])

        print(f"File id is {self.node_uuid} type is {self.file_type}")
        if self.magic_number != 0x00105555:
            print("Data node magic is wrong")

        if self.data_additional_block_pointer != 0:
            additional_data_list = [NodeAdditionalData(file, self.data_additional_block_pointer)]
            i = 1
            while additional_data_list[i - 1].data_additional_block_pointer != 0:
                try:
                    additional_data_list.append(
                        NodeAdditionalData(file, additional_data_list[i - 1].data_additional_block_pointer))
                except Exception as e:
                    print("File content does not meet specification.")
                    break
                i += 1
            self.total_byte_array_with_additional_blocks = self.append_byte_arrays(self.bytes, additional_data_list)
        else:
            self.total_byte_array_with_additional_blocks = self.bytes[1:]

    @staticmethod
    def append_byte_arrays(original, object_list):
        total_length = len(original) - 1
        for obj in object_list:
            total_length += len(obj.bytes)

        result = bytearray(total_length)

        result[0:len(original) - 1] = original[1:]

        current_pos = len(original) - 1
        for obj in object_list:
            byte_array = obj.bytes
            result[current_pos:current_pos + len(byte_array)] = byte_array
            current_pos += len(byte_array)

        return bytes(result)


class NodeEntriesAsList:
    def __init__(self, file, data_nodes, file_metadata_map):
        self.total_entries = read_int(file)
        self.child_node_entries = read_int(file)
        self.data_entry_count = read_int(file)
        self.additional_entries_position = read_pointer(file)

        print(
            f"NodeEntriesAsList: Read list entries fields. totalEntries: {self.total_entries}, childNodeEntries: {self.child_node_entries}, dataEntryCount: {self.data_entry_count}")

        self.child_entries = [NodeEntry(file) for _ in range(self.child_node_entries)]

        skip_bytes = (self.total_entries - self.child_node_entries - self.data_entry_count) * (8 + 4)
        print(f"NodeEntriesAsList: Skipping {skip_bytes} bytes of empty space.")
        file.seek(file.tell() + skip_bytes)  # Skip empty space
        print(f"Current position: {file.tell()}")

        self.data_entries_list = [NodeEntry(file) for _ in range(self.data_entry_count)]

        for child_node in self.child_entries:
            file.seek(child_node.position)
            Node(file, data_nodes)

        data_nodes.extend([DataNode(file, entry, file_metadata_map) for entry in self.data_entries_list])
        
        if self.additional_entries_position:
            file.seek(self.additional_entries_position + 4)
            self.additional_entries = NodeEntriesAsList(file, data_nodes, file_metadata_map)

    def count_nodes(self):
        return len(self.child_entries)


class MetadataContentEntry:
    def __init__(self, file):
        self.name_length = read_int(file)
        self.entry_name = read_string(file, self.name_length)
        self.entry_type = read_int(file)
        self.data = self.read_data(file, self.entry_type)

        print(
            f"MetadataContentEntry: Read nameLength: {self.name_length}, entry name: {self.entry_name}, entry type: {self.entry_type}, data: {self.data}")

    def read_data(self, file, entry_type):
        if entry_type == -1:  # boolean
            return read_boolean(file)
        elif entry_type == -2:  # long
            return read_long(file)
        elif entry_type == -3:  # double
            return read_double(file)
        elif entry_type == -4:  # raw data
            data_length = read_int(file)
            return read_fully(file, data_length)
        else:  # string
            return read_string(file, entry_type)


class MetadataContent:
    def __init__(self, file, version):
        self.size = read_int(file)
        self.entries = []

        for i in range(self.size):
            try:
                self.entries.append(MetadataContentEntry(file))
            except Exception as e:
                print("Metadata content does not meet doc specification")
                break

        print(f"MetadataContent: Read size: {self.size}")


class Metadata:
    def __init__(self, file, version):
        self.main_content = MetadataContent(file, version)

        if self.main_content.size < 0:
            return

        if version == 3 and self.main_content.size >= 0:
            read_int(file)

        if version >= 2:
            self.ext_count = read_int(file)
            if self.ext_count > 0:  # typically -1 in most files, typically 0 in LDK files
                print("Extended metadata will not be processed")


class Node:
    def __init__(self, file, data_node_list):
        self.magic_number = read_int(file)
        self.flags = read_int(file)
        self.metadata_position = read_pointer(file)
        self.reserved = read_double(file)

        if self.magic_number == 0x00015555:
            print("Node magic is wrong")

        current_position = file.tell()
        if current_position != self.metadata_position:
            print(f"Node: Seeking to metadataPosition at {self.metadata_position}")
            file.seek(self.metadata_position + 0x20)

        self.metadata = Metadata(file, 1)
        file.seek(current_position)

        file_metadata_map = {entry.entry_name: str(entry.data) for entry in self.metadata.main_content.entries}

        self.entries = NodeEntries(file, data_node_list, file_metadata_map)

    def count_nodes(self):
        count = 1  # Count this node
        if self.entries:
            count += self.entries.count_nodes()
        return count


class NodeEntriesAsTable:
    def __init__(self, file, data_nodes, file_metadata_map):
        self.child_node_entries = read_int(file)
        self.data_entry_count = read_int(file)

        print(
            f"NodeEntriesAsTable: Read table entries fields. childNodeEntries: {self.child_node_entries}, dataEntryCount: {self.data_entry_count}")

        self.child_entries = [NodeEntry(file) for _ in range(self.child_node_entries)]
        self.data_entries_list = [NodeEntry(file) for _ in range(self.data_entry_count)]

        data_nodes.extend(DataNode(file, entry, file_metadata_map) for entry in self.data_entries_list)

        for child_node in self.child_entries:
            file.seek(child_node.position)
            Node(file, data_nodes)

    def count_nodes(self):
        return len(self.child_entries)


class NodeEntries:
    def __init__(self, file, data_node_list, file_metadata_map):
        self.magic_number = read_int(file)
        print(f"NodeEntries: Read magicNumber: {self.magic_number}")

        self.list_entries = None
        self.table_entries = None

        if self.magic_number == 0x00025555:
            self.list_entries = NodeEntriesAsList(file, data_node_list, file_metadata_map)
        elif self.magic_number == 0x00045555:
            self.table_entries = NodeEntriesAsTable(file, data_node_list, file_metadata_map)

    def count_nodes(self):
        count = 0
        if self.list_entries is not None:
            count += self.list_entries.count_nodes()
        if self.table_entries is not None:
            count += self.table_entries.count_nodes()
        return count


class LdkFile:
    def __init__(self, file):
        self.magic_number = read_int(file)
        self.archive_version = read_int(file)
        self.root_node_position = read_pointer(file)
        self.reserved1 = read_double(file)
        self.reserved2 = read_double(file)
        self.reserved3 = read_double(file)
        self.reserved4 = read_double(file)

        print("LdkFile: Read header fields.")

        file.seek(self.root_node_position)
        print(f"LdkFile: Seeking to rootNodePosition at {self.root_node_position}")
        self.data_nodes = []
        self.root_node = Node(file, self.data_nodes)

    def count_nodes(self):
        return self.root_node.count_nodes()
