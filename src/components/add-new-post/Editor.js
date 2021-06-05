import React from "react";
import ReactQuill from "react-quill";
import { Card, CardBody, Form, FormInput } from "shards-react";

import "react-quill/dist/quill.snow.css";
import "../../assets/quill.css";

const Editor = () => (
  <Card small className="mb-3">
    <CardBody>
      <Form className="add-new-post" action="" method="POST">
        <FormInput size="lg" className="mb-3" placeholder="Your Post Title" />
        <ReactQuill className="add-new-post__editor mb-1" />
        <button class="ml-auto btn btn-accent btn-sm" type="submit"><i class="material-icons">file_copy</i> Publish</button>
      </Form>
    </CardBody>
  </Card>
);

export default Editor;
