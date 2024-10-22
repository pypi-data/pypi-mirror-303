from argparse import ArgumentParser, FileType

def cli_setup():
    base_options = ArgumentParser()
    base_options.add_argument('--input-p12-path', '-k', type=FileType('r'))
    base_options.add_argument('--input-p12-password', '-p', default='changeit')
    base_options.add_argument('--config', '-L', default='libcertifier.cfg')
    base_options.add_argument('--verbose', '-v', action='store_true')

    get_crt_token_options = ArgumentParser(add_help=False)
    get_crt_token_options.add_argument('--auth-type', '-X')
    get_crt_token_options.add_argument('--auth-token', '-S')

    get_cert_long_options = ArgumentParser(add_help=False)
    get_cert_long_options.add_argument('--crt', '-T')
    get_cert_long_options.add_argument('--output-p12-path', '-o')
    get_cert_long_options.add_argument('--output-p12-password', '-w')
    get_cert_long_options.add_argument('--product-id', '-i',)
    get_cert_long_options.add_argument('--node-id', '-n')
    get_cert_long_options.add_argument('--fabric-id', '-F')
    get_cert_long_options.add_argument('--case-auth-tag', '-a')
    get_cert_long_options.add_argument('--overwrite-p12', '-f', action='store_true')
    get_cert_long_options.add_argument('--profile-name', '-P')

    validity_days_long_option = ArgumentParser(add_help=False)
    validity_days_long_option.add_argument('--validity_days', '-t')

    ca_path_long_option = ArgumentParser(add_help=False)
    ca_path_long_option.add_argument('--ca-path', '-c', type=FileType('r'))

    arg_parser = ArgumentParser()
    subparsers = arg_parser.add_subparsers(dest='command', required=True)

    subparsers.add_parser('get-cert', parents=[base_options, get_crt_token_options, get_cert_long_options, 
                                     validity_days_long_option, ca_path_long_option], add_help=False)
    
    subparsers.add_parser('get-crt-token', parents=[base_options, get_crt_token_options], add_help=False)

    subparsers.add_parser('get-cert-status', parents=[base_options, ca_path_long_option], add_help=False)
    
    subparsers.add_parser('get-cert-validity', parents=[base_options, ca_path_long_option], add_help=False)
    
    subparsers.add_parser('renew-cert', parents=[base_options, ca_path_long_option], add_help=False)
    
    subparsers.add_parser('print-cert', parents=[base_options], add_help=False)
    
    subparsers.add_parser('revoke', parents=[base_options, ca_path_long_option], add_help=False)

    return arg_parser