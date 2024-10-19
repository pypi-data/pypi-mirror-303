from typing import Any, Final

from zargunlite.model import ZircoliteFieldMappingConfig, ZircoliteFieldMappingSplitConfig

_default_field_mapping_config_data: Final[dict[str, Any]] = {
    "exclusions": ["xmlns"],
    "useless": [None, ""],
    "mappings": {
        "Event.EventData.UserData": "UserData",
        "Event.System.Provider.#attributes.Guid": "Guid",
        "Event.EventData.ContextInfo": "ContextInfo",
        "Event.System.Execution.#attributes.ProcessID": "ProcessID",
        "Event.System.Execution.#attributes.ThreadID": "ThreadID",
        "Event.System.EventID": "EventID",
        "Event.System.EventID.#text": "EventID",
        "Event.System.Channel": "Channel",
        "Event.System.Computer": "Computer",
        "Event.System.Correlation": "Correlation",
        "Event.System.Correlation.#attributes.ActivityID": "ActivityID",
        "Event.System.EventID.#attributes.Qualifiers": "Qualifiers",
        "Event.System.EventRecordID": "EventRecordID",
        "Event.System.Keywords": "Keywords",
        "Event.System.Level": "Level",
        "Event.System.Opcode": "Opcode",
        "Event.System.Provider.#attributes.EventSourceName": "EventSourceName",
        "Event.System.Provider.#attributes.Name": "Provider_Name",
        "Event.System.Security": "Security",
        "Event.System.Security.#attributes.UserID": "UserID",
        "Event.System.Task": "Task",
        "Event.System.TimeCreated.#attributes.SystemTime": "SystemTime",
        "Event.System.Version": "Version",
        "Event.EventData.AccessList": "AccessList",
        "Event.EventData.AccessMask": "AccessMask",
        "Event.EventData.Accesses": "Accesses",
        "Event.EventData.AccountDomain": "AccountDomain",
        "Event.EventData.AccountExpires": "AccountExpires",
        "Event.EventData.AccountName": "AccountName",
        "Event.EventData.AddonName": "AddonName",
        "Event.EventData.Address": "Address",
        "Event.EventData.AddressLength": "AddressLength",
        "Event.EventData.AllowedToDelegateTo": "AllowedToDelegateTo",
        "Event.EventData.Application": "Application",
        "Event.EventData.AttributeLDAPDisplayName": "AttributeLDAPDisplayName",
        "Event.EventData.AttributeValue": "AttributeValue",
        "Event.EventData.AuditPolicyChanges": "AuditPolicyChanges",
        "Event.EventData.AuditSourceName": "AuditSourceName",
        "Event.EventData.AuthenticationPackageName": "AuthenticationPackageName",
        "Event.EventData.Binary": "Binary",
        "Event.EventData.BootMode": "BootMode",
        "Event.EventData.BuildVersion": "BuildVersion",
        "Event.EventData.CallingProcessName": "CallingProcessName",
        "Event.EventData.CallTrace": "CallTrace",
        "Event.EventData.CommandLine": "CommandLine",
        "Event.EventData.Company": "Company",
        "Event.EventData.Context": "Context",
        "Event.EventData.CreationUtcTime": "CreationUtcTime",
        "Event.EventData.CurrentDirectory": "CurrentDirectory",
        "Event.EventData.DCName": "DCName",
        "Event.EventData.Description": "Description",
        "Event.EventData.DestinationAddress": "DestinationAddress",
        "Event.EventData.DestinationHostname": "DestinationHostname",
        "Event.EventData.DestinationIp": "DestinationIp",
        "Event.EventData.DestinationIsIpv6": "DestinationIsIpv6",
        "Event.EventData.DestinationPort": "DestinationPort",
        "Event.EventData.DestinationPortName": "DestinationPortName",
        "Event.EventData.DestPort": "DestPort",
        "Event.EventData.Detail": "Detail",
        "Event.EventData.Details": "Details",
        "Event.EventData.DetectionSource": "DetectionSource",
        "Event.EventData.DeviceClassName": "DeviceClassName",
        "Event.EventData.DeviceDescription": "DeviceDescription",
        "Event.EventData.DeviceName": "DeviceName",
        "Event.EventData.DeviceNameLength": "DeviceNameLength",
        "Event.EventData.DeviceTime": "DeviceTime",
        "Event.EventData.DeviceVersionMajor": "DeviceVersionMajor",
        "Event.EventData.DeviceVersionMinor": "DeviceVersionMinor",
        "Event.EventData.DisplayName": "DisplayName",
        "Event.EventData.EngineVersion": "EngineVersion",
        "Event.EventData.ErrorCode": "ErrorCode",
        "Event.EventData.ErrorDescription": "ErrorDescription",
        "Event.EventData.ErrorMessage": "ErrorMessage",
        "Event.EventData.EventSourceId": "EventSourceId",
        "Event.EventData.EventType": "EventType",
        "Event.EventData.ExtensionId": "ExtensionId",
        "Event.EventData.ExtensionName": "ExtensionName",
        "Event.EventData.ExtraInfo": "ExtraInfo",
        "Event.EventData.FailureCode": "FailureCode",
        "Event.EventData.FailureReason": "FailureReason",
        "Event.EventData.FileVersion": "FileVersion",
        "Event.EventData.FilterHostProcessID": "FilterHostProcessID",
        "Event.EventData.FinalStatus": "FinalStatus",
        "Event.EventData.GrantedAccess": "GrantedAccess",
        "Event.EventData.Group": "Group",
        "Event.EventData.GroupDomain": "GroupDomain",
        "Event.EventData.GroupName": "GroupName",
        "Event.EventData.GroupSid": "GroupSid",
        "Event.EventData.HandleId": "HandleId",
        "Event.EventData.Hash": "Hash",
        "Event.EventData.Hashes": "Hashes",
        "Event.EventData.HiveName": "HiveName",
        "Event.EventData.HomeDirectory": "HomeDirectory",
        "Event.EventData.HomePath": "HomePath",
        "Event.EventData.HostApplication": "HostApplication",
        "Event.EventData.HostName": "HostName",
        "Event.EventData.HostVersion": "HostVersion",
        "Event.EventData.IdleStateCount": "IdleStateCount",
        "Event.EventData.Image": "Image",
        "Event.EventData.ImageLoaded": "ImageLoaded",
        "Event.EventData.ImagePath": "ImagePath",
        "Event.EventData.Initiated": "Initiated",
        "Event.EventData.IntegrityLevel": "IntegrityLevel",
        "Event.EventData.IpAddress": "IpAddress",
        "Event.EventData.IpPort": "IpPort",
        "Event.EventData.KeyLength": "KeyLength",
        "Event.EventData.LayerRTID": "LayerRTID",
        "Event.EventData.LDAPDisplayName": "LDAPDisplayName",
        "Event.EventData.LmPackageName": "LmPackageName",
        "Event.EventData.LogonGuid": "LogonGuid",
        "Event.EventData.LogonHours": "LogonHours",
        "Event.EventData.LogonId": "LogonId",
        "Event.EventData.LogonProcessName": "LogonProcessName",
        "Event.EventData.LogonType": "LogonType",
        "Event.EventData.MajorVersion": "MajorVersion",
        "Event.EventData.Data.#text": "Message",
        "Event.EventData.MinorVersion": "MinorVersion",
        "Event.EventData.NewName": "NewName",
        "Event.EventData.NewProcessId": "NewProcessId",
        "Event.EventData.NewProcessName": "NewProcessName",
        "Event.EventData.NewState": "NewState",
        "Event.EventData.NewThreadId": "NewThreadId",
        "Event.EventData.NewTime": "NewTime",
        "Event.EventData.NewUacValue": "NewUacValue",
        "Event.EventData.NewValue": "NewValue",
        "Event.EventData.NotificationPackageName": "NotificationPackageName",
        "Event.EventData.Number": "Number",
        "Event.EventData.NumberOfGroupPolicyObjects": "NumberOfGroupPolicyObjects",
        "Event.EventData.ObjectClass": "ObjectClass",
        "Event.EventData.ObjectName": "ObjectName",
        "Event.EventData.ObjectServer": "ObjectServer",
        "Event.EventData.ObjectType": "ObjectType",
        "Event.EventData.ObjectValueName": "ObjectValueName",
        "Event.EventData.OldTime": "OldTime",
        "Event.EventData.OldUacValue": "OldUacValue",
        "Event.EventData.OperationType": "OperationType",
        "Event.EventData.OriginalFileName": "OriginalFileName",
        "Event.EventData.PackageName": "PackageName",
        "Event.EventData.ParentCommandLine": "ParentCommandLine",
        "Event.EventData.ParentImage": "ParentImage",
        "Event.EventData.ParentProcessGuid": "ParentProcessGuid",
        "Event.EventData.ParentProcessId": "ParentProcessId",
        "Event.EventData.PasswordLastSet": "PasswordLastSet",
        "Event.EventData.Payload": "Payload",
        "Event.EventData.PerfStateCount": "PerfStateCount",
        "Event.EventData.PipeName": "PipeName",
        "Event.EventData.PreviousTime": "PreviousTime",
        "Event.EventData.PrimaryGroupId": "PrimaryGroupId",
        "Event.EventData.PrivilegeList": "PrivilegeList",
        "Event.EventData.ProcessCommandLine": "ProcessCommandLine",
        "Event.EventData.ProcessGuid": "ProcessGuid",
        "Event.EventData.ProcessId": "ProcessId",
        "Event.EventData.ProcessName": "ProcessName",
        "Event.EventData.ProcessingMode": "ProcessingMode",
        "Event.EventData.ProcessingTimeInMilliseconds": "ProcessingTimeInMilliseconds",
        "Event.EventData.Product": "Product",
        "Event.EventData.ProfilePath": "ProfilePath",
        "Event.EventData.Properties": "Properties",
        "Event.EventData.Protocol": "Protocol",
        "Event.EventData.ProtocolHostProcessID": "ProtocolHostProcessID",
        "Event.EventData.PuaCount": "PuaCount",
        "Event.EventData.PuaPolicyId": "PuaPolicyId",
        "Event.EventData.Publisher": "Publisher",
        "Event.EventData.QfeVersion": "QfeVersion",
        "Event.EventData.QueryName": "QueryName",
        "Event.EventData.QueryResults": "QueryResults",
        "Event.EventData.QueryStatus": "QueryStatus",
        "Event.EventData.RelativeTargetName": "RelativeTargetName",
        "Event.EventData.ResourceManager": "ResourceManager",
        "Event.EventData.RetryMinutes": "RetryMinutes",
        "Event.EventData.RuleName": "RuleName",
        "Event.EventData.SamAccountName": "SAMAccountName",
        "Event.EventData.SchemaVersion": "SchemaVersion",
        "Event.EventData.ScriptPath": "ScriptPath",
        "Event.EventData.ScriptBlockText": "ScriptBlockText",
        "Event.EventData.SecurityPackageName": "SecurityPackageName",
        "Event.EventData.ServerID": "ServerID",
        "Event.EventData.ServerURL": "ServerURL",
        "Event.EventData.Service": "Service",
        "Event.EventData.ServiceName": "ServiceName",
        "Event.EventData.ServicePrincipalNames": "ServicePrincipalNames",
        "Event.EventData.ServiceType": "ServiceType",
        "Event.EventData.ServiceVersion": "ServiceVersion",
        "Event.EventData.ShareLocalPath": "ShareLocalPath",
        "Event.EventData.ShareName": "ShareName",
        "Event.EventData.ShutdownActionType": "ShutdownActionType",
        "Event.EventData.ShutdownEventCode": "ShutdownEventCode",
        "Event.EventData.ShutdownReason": "ShutdownReason",
        "Event.EventData.SidHistory": "SidHistory",
        "Event.EventData.Signature": "Signature",
        "Event.EventData.SignatureStatus": "SignatureStatus",
        "Event.EventData.Signed": "Signed",
        "Event.EventData.SourceAddress": "SourceAddress",
        "Event.EventData.SourceHostname": "SourceHostname",
        "Event.EventData.SourceImage": "SourceImage",
        "Event.EventData.SourceIp": "SourceIp",
        "Event.EventData.SourceNetworkAddress": "SourceNetworkAddress",
        "Event.EventData.SourceIsIpv6": "SourceIsIpv6",
        "Event.EventData.SourcePort": "SourcePort",
        "Event.EventData.SourcePortName": "SourcePortName",
        "Event.EventData.SourceProcessGuid": "SourceProcessGuid",
        "Event.EventData.SourceProcessId": "SourceProcessId",
        "Event.EventData.StartAddress": "StartAddress",
        "Event.EventData.StartFunction": "StartFunction",
        "Event.EventData.StartModule": "StartModule",
        "Event.EventData.StartTime": "StartTime",
        "Event.EventData.StartType": "StartType",
        "Event.EventData.State": "State",
        "Event.EventData.Status": "Status",
        "Event.EventData.StopTime": "StopTime",
        "Event.EventData.SubStatus": "SubStatus",
        "Event.EventData.SubjectDomainName": "SubjectDomainName",
        "Event.EventData.SubjectLogonId": "SubjectLogonId",
        "Event.EventData.SubjectUserName": "SubjectUserName",
        "Event.EventData.SubjectUserSid": "SubjectUserSid",
        "Event.EventData.TSId": "TSId",
        "Event.EventData.TargetDomainName": "TargetDomainName",
        "Event.EventData.TargetFilename": "TargetFileName",
        "Event.EventData.TargetImage": "TargetImage",
        "Event.EventData.TargetInfo": "TargetInfo",
        "Event.EventData.TargetLogonGuid": "TargetLogonGuid",
        "Event.EventData.TargetLogonId": "TargetLogonId",
        "Event.EventData.TargetObject": "TargetObject",
        "Event.EventData.TargetProcessAddress": "TargetProcessAddress",
        "Event.EventData.TargetProcessGuid": "TargetProcessGuid",
        "Event.EventData.TargetProcessId": "TargetProcessId",
        "Event.EventData.TargetServerName": "TargetServerName",
        "Event.EventData.TargetSid": "TargetSid",
        "Event.EventData.TargetUserName": "TargetUserName",
        "Event.EventData.TargetUserSid": "TargetUserSid",
        "Event.EventData.TaskContent": "TaskContent",
        "Event.EventData.TaskContentNew": "TaskContentNew",
        "Event.EventData.TaskName": "TaskName",
        "Event.EventData.TerminalSessionId": "TerminalSessionId",
        "Event.EventData.ThrottleStateCount": "ThrottleStateCount",
        "Event.EventData.TicketEncryptionType": "TicketEncryptionType",
        "Event.EventData.TicketOptions": "TicketOptions",
        "Event.EventData.TimeSource": "TimeSource",
        "Event.EventData.TokenElevationType": "TokenElevationType",
        "Event.EventData.TransactionId": "TransactionId",
        "Event.EventData.TransmittedServices": "TransmittedServices",
        "Event.EventData.User": "User",
        "Event.EventData.UserAccountControl": "UserAccountControl",
        "Event.EventData.UserParameters": "UserParameters",
        "Event.EventData.UserPrincipalName": "UserPrincipalName",
        "Event.EventData.UserSid": "UserSid",
        "Event.EventData.UserWorkstations": "UserWorkstations",
        "Event.EventData.UtcTime": "UtcTime",
        "Event.EventData.Version": "Version",
        "Event.EventData.Workstation": "Workstation",
        "Event.EventData.WorkstationName": "WorkstationName",
        "Event.EventData.updateGuid": "updateGuid",
        "Event.EventData.updateRevisionNumber": "updateRevisionNumber",
        "Event.EventData.updateTitle": "updateTitle",
        "Event.EventData.ParentIntegrityLevel": "ParentIntegrityLevel",
        "Event.EventData.ParentUser": "ParentUser",
    },
    "alias": {},
    "split": {
        "Hash": {"separator": ",", "equal": "="},
        "Hashes": {"separator": ",", "equal": "="},
        "ConfigurationFileHash": {"separator": ",", "equal": "="},
    },
}

DEFAULT_FIELD_MAPPING_CONFIG: Final = ZircoliteFieldMappingConfig(
    exclusions=_default_field_mapping_config_data["exclusions"],
    useless=_default_field_mapping_config_data["useless"],
    mappings=_default_field_mapping_config_data["mappings"],
    alias=_default_field_mapping_config_data["alias"],
    split={
        k: ZircoliteFieldMappingSplitConfig(separator=v["separator"], equal=v["equal"])
        for k, v in _default_field_mapping_config_data["split"].items()
    },
)

EMPTY_FIELD_MAPPING_CONFIG: Final = ZircoliteFieldMappingConfig()
