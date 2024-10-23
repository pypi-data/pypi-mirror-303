import {
  LabelTypeEditRecord,
  LabelTypeDeleteRecord,
  LabelTypePublishRecord,
  LabelTypeRecordNewVersion,
} from "./labels/TypeLabels";
import {
  PublishRecordIcon,
  DeleteRecordIcon,
  EditRecordIcon,
  RecordNewVersionIcon,
} from "./icons/TypeIcons";

export const requestTypeSpecificComponents = {
  [`RequestTypeLabel.layout.edit_published_record`]: LabelTypeEditRecord,
  [`RequestTypeLabel.layout.delete_published_record`]: LabelTypeDeleteRecord,
  [`RequestTypeLabel.layout.publish_draft`]: LabelTypePublishRecord,
  [`RequestTypeLabel.layout.new_version`]: LabelTypeRecordNewVersion,
  [`InvenioRequests.RequestTypeIcon.layout.edit_published_record`]:
    EditRecordIcon,
  [`InvenioRequests.RequestTypeIcon.layout.delete_published_record`]:
    DeleteRecordIcon,
  [`InvenioRequests.RequestTypeIcon.layout.publish_draft`]: PublishRecordIcon,
  PublishRecordIcon,
  [`InvenioRequests.RequestTypeIcon.layout.new_version`]: RecordNewVersionIcon,
};
