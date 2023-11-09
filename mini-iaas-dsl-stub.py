from collections import namedtuple
import re

# Define the command structure as a namedtuple for easy access
Command = namedtuple('Command', ['action', 'parameters'])

# Abstract base class for cloud platform implementations
class CloudPlatform:
    def create_instance(self, parameters):
        raise NotImplementedError

    def read_instance(self, instance_id):
        raise NotImplementedError

    def update_instance(self, parameters):
        raise NotImplementedError

    def delete_instance(self, instance_id):
        raise NotImplementedError

    def monitor_instance(self, parameters):
        raise NotImplementedError

    def health_check_instance(self, parameters):
        raise NotImplementedError

    def report_problem_instance(self, parameters):
        raise NotImplementedError

    def scale_instance(self, parameters):
        raise NotImplementedError

    def snapshot_instance(self, parameters):
        raise NotImplementedError

    def restore_instance(self, parameters):
        raise NotImplementedError

    def configure_network_instance(self, parameters):
        raise NotImplementedError

    def attach_storage_instance(self, parameters):
        raise NotImplementedError

    def detach_storage_instance(self, parameters):
        raise NotImplementedError

# Concrete implementations for each cloud platform
class AWSPlatform(CloudPlatform):
    def create_instance(self, parameters):
        print(f"AWS: Creating instance with parameters: {parameters}")

    def read_instance(self, instance_id):
        print(f"AWS: Reading instance with ID: {instance_id}")

    def update_instance(self, parameters):
        print(f"AWS: Updating instance with parameters: {parameters}")

    def delete_instance(self, instance_id):
        print(f"AWS: Deleting instance with ID: {instance_id}")

    def monitor_instance(self, parameters):
        print(f"AWS: Monitoring instance with parameters: {parameters}")

    def health_check_instance(self, parameters):
        print(f"AWS: Health check for instance with parameters: {parameters}")

    def report_problem_instance(self, parameters):
        print(f"AWS: Reporting problem for instance with parameters: {parameters}")

    def scale_instance(self, parameters):
        print(f"AWS: Scaling instance with parameters: {parameters}")

    def snapshot_instance(self, parameters):
        print(f"AWS: Taking snapshot with parameters: {parameters}")

    def restore_instance(self, parameters):
        print(f"AWS: Restoring instance with parameters: {parameters}")

    def configure_network_instance(self, parameters):
        print(f"AWS: Configuring network for instance with parameters: {parameters}")

    def attach_storage_instance(self, parameters):
        print(f"AWS: Attaching storage to instance with parameters: {parameters}")

    def detach_storage_instance(self, parameters):
        print(f"AWS: Detaching storage from instance with parameters: {parameters}")

class AzurePlatform(CloudPlatform):
    def create_instance(self, parameters):
        print(f"Azure: Creating instance with parameters: {parameters}")

    def read_instance(self, instance_id):
        print(f"Azure: Reading instance with ID: {instance_id}")

    def update_instance(self, parameters):
        print(f"Azure: Updating instance with parameters: {parameters}")

    def delete_instance(self, instance_id):
        print(f"Azure: Deleting instance with ID: {instance_id}")

    def monitor_instance(self, parameters):
        print(f"Azure: Monitoring instance with parameters: {parameters}")

    def health_check_instance(self, parameters):
        print(f"Azure: Health check for instance with parameters: {parameters}")

    def report_problem_instance(self, parameters):
        print(f"Azure: Reporting problem for instance with parameters: {parameters}")

    def scale_instance(self, parameters):
        print(f"Azure: Scaling instance with parameters: {parameters}")

    def snapshot_instance(self, parameters):
        print(f"Azure: Taking snapshot with parameters: {parameters}")

    def restore_instance(self, parameters):
        print(f"Azure: Restoring instance with parameters: {parameters}")

    def configure_network_instance(self, parameters):
        print(f"Azure: Configuring network for instance with parameters: {parameters}")

    def attach_storage_instance(self, parameters):
        print(f"Azure: Attaching storage to instance with parameters: {parameters}")

    def detach_storage_instance(self, parameters):
        print(f"Azure: Detaching storage from instance with parameters: {parameters}")

class GCPPlatform(CloudPlatform):
    def create_instance(self, parameters):
        print(f"GCP: Creating instance with parameters: {parameters}")

    def read_instance(self, instance_id):
        print(f"GCP: Reading instance with ID: {instance_id}")

    def update_instance(self, parameters):
        print(f"GCP: Updating instance with parameters: {parameters}")

    def delete_instance(self, instance_id):
        print(f"GCP: Deleting instance with ID: {instance_id}")

    def monitor_instance(self, parameters):
        print(f"GCP: Monitoring instance with parameters: {parameters}")

    def health_check_instance(self, parameters):
        print(f"GCP: Health check for instance with parameters: {parameters}")

    def report_problem_instance(self, parameters):
        print(f"GCP: Reporting problem for instance with parameters: {parameters}")

    def scale_instance(self, parameters):
        print(f"GCP: Scaling instance with parameters: {parameters}")

    def snapshot_instance(self, parameters):
        print(f"GCP: Taking snapshot with parameters: {parameters}")

    def restore_instance(self, parameters):
        print(f"GCP: Restoring instance with parameters: {parameters}")

    def configure_network_instance(self, parameters):
        print(f"GCP: Configuring network for instance with parameters: {parameters}")

    def attach_storage_instance(self, parameters):
        print(f"GCP: Attaching storage to instance with parameters: {parameters}")

    def detach_storage_instance(self, parameters):
        print(f"GCP: Detaching storage from instance with parameters: {parameters}")

# Factory function to return the concrete implementation
def get_platform_implementation(platform_name):
    if platform_name == 'AWS':
        return AWSPlatform()
    elif platform_name == 'Azure':
        return AzurePlatform()
    elif platform_name == 'GCP':
        return GCPPlatform()
    else:
        raise ValueError(f"Unknown platform: {platform_name}")

# Helper function to parse parameters into a dictionary
def parse_parameters(parameter_string):
    parameters = dict(item.split('=') for item in parameter_string.split(', '))
    return parameters

# Parser function to parse the DSL command
def parse_command(command_string):
    match = re.match(r"(\w+)\s(.+)", command_string)
    if not match:
        raise ValueError(f"Invalid command format: {command_string}")

    action, parameter_string = match.groups()
    parameters = parse_parameters(parameter_string)
    return Command(action=action, parameters=parameters)

# Validator functions for each command
def validate_create(parameters):
    required_params = {'type', 'region', 'os', 'storage'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for create: {missing}")

# Validator functions for each command
def validate_create(parameters):
    required_params = {'type', 'region', 'os', 'storage'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for create: {missing}")

def validate_read(parameters):
    required_params = {'instance_id'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for read: {missing}")

def validate_update(parameters):
    required_params = {'instance_id'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for update: {missing}")

def validate_delete(parameters):
    required_params = {'instance_id'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for delete: {missing}")

def validate_monitor(parameters):
    required_params = {'instance_id', 'metric', 'threshold', 'interval'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for monitor: {missing}")

def validate_health_check(parameters):
    required_params = {'instance_id', 'check_type', 'endpoint', 'frequency'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for health_check: {missing}")

def validate_report_problem(parameters):
    required_params = {'instance_id', 'issue_description'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for report_problem: {missing}")

def validate_scale(parameters):
    required_params = {'instance_id', 'cpu', 'memory'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for scale: {missing}")

def validate_snapshot(parameters):
    required_params = {'instance_id', 'snapshot_name'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for snapshot: {missing}")

def validate_restore(parameters):
    required_params = {'instance_id', 'snapshot_id'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for restore: {missing}")

def validate_configure_network(parameters):
    required_params = {'instance_id', 'vpc', 'subnet', 'security_group'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for configure_network: {missing}")

def validate_attach_storage(parameters):
    required_params = {'instance_id', 'volume_id', 'mount_point'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for attach_storage: {missing}")

def validate_detach_storage(parameters):
    required_params = {'instance_id', 'volume_id'}
    if not required_params.issubset(parameters):
        missing = required_params - set(parameters)
        raise ValueError(f"Missing parameters for detach_storage: {missing}")

# Main validator function that dispatches to specific validators
def validate_command(command):
    validator_map = {
        'create': validate_create,
        'read': validate_read,
        'update': validate_update,
        'delete': validate_delete,
        'monitor': validate_monitor,
        'health_check': validate_health_check,
        'report_problem': validate_report_problem,
        'scale': validate_scale,
        'snapshot': validate_snapshot,
        'restore': validate_restore,
        'configure_network': validate_configure_network,
        'attach_storage': validate_attach_storage,
        'detach_storage': validate_detach_storage,
    }

    validator = validator_map.get(command.action)
    if not validator:
        raise ValueError(f"Unsupported action: {command.action}")

    validator(command.parameters)

# Executor function to execute the DSL command
def execute_command(command, platform_implementation):
    action_map = {
        'create': platform_implementation.create_instance,
        'read': platform_implementation.read_instance,
        'update': platform_implementation.update_instance,
        'delete': platform_implementation.delete_instance,
        'monitor': platform_implementation.monitor_instance,
        'health_check': platform_implementation.health_check_instance,
        'report_problem': platform_implementation.report_problem_instance,
        'scale': platform_implementation.scale_instance,
        'snapshot': platform_implementation.snapshot_instance,
        'restore': platform_implementation.restore_instance,
        'configure_network': platform_implementation.configure_network_instance,
        'attach_storage': platform_implementation.attach_storage_instance,
        'detach_storage': platform_implementation.detach_storage_instance,
    }

    action = action_map.get(command.action)
    if not action:
        raise ValueError(f"Unsupported action: {command.action}")

    action(command.parameters)

# Main function to tie it all together
def main(command_string, platform_name):
    platform_implementation = get_platform_implementation(platform_name)
    command = parse_command(command_string)
    validate_command(command)
    execute_command(command, platform_implementation)

# Example usage
if __name__ == "__main__":
    command_string = "create type=t2.large, region=us-west-1, os=linux, storage=500GB"
    platform_name = 'AWS'  # Or 'Azure' or 'GCP'
    main(command_string, platform_name)
