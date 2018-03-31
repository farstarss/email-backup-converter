import os

# define encoding for files
USE_ENCODING = 'ansi'
# define folders
FOLDER_EMAIL_BACKUP = 'backup'
FOLDER_CONVERTED_EMAILS = 'converted'
# define file extension
BACKUP_EXTENSION = 'txt'

# init email counter
email_count = 0

# parse all files in backup folder
for file in os.listdir(FOLDER_EMAIL_BACKUP):
    # only process txt files
    if file.endswith(".{}".format(BACKUP_EXTENSION)):
        # file name
        fn = os.path.join(FOLDER_EMAIL_BACKUP, file)
        # init file write handler
        f_w = None

        line_id = 0
        # print file we are processing
        print("Processing:", fn)
        # open file
        with open(fn, 'r', encoding=USE_ENCODING, errors='replace') as f_r:
            # reset printed_error state with each file
            printed_error = False
            # process every line
            for content in f_r:
                line_id += 1
                # 'From ' identifies the beginning of a new email
                if content[:5] == 'From ':
                    # close old file write handler
                    if f_w is not None:
                        f_w.close()
                    # increase email counter
                    email_count += 1
                    # build destination path
                    dest_file_name = '{}-{}.txt'.format(file, email_count)
                    dest_path = os.path.join(FOLDER_CONVERTED_EMAILS, dest_file_name)
                    # open new email file in binary mode to avoid encoding issues
                    f_w = open(dest_path, 'wb')
                # make sure we got a valid file handler and, prior to this, got the right content
                if f_w is None:
                    if not printed_error:
                        printed_error = True
                        print("Error in line {} in {}. Expected 'From ', got '{}'".format(line_id, fn, content))
                    continue
                # write read content as bitarray
                f_w.write(bytearray(content, encoding=USE_ENCODING, errors='replace'))
                

# print result
print("Done converting {} emails.".format(email_count))
